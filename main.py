from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    story: Annotated[list, add_messages]
    control: str

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.8)

def system_prompt() -> str:
    system_prompt = """
    You are a helpful assistant that provides next 1-2 new lines of a story.
    You are going to add the story with the next 1-2 new lines.
    Remember, you need to add maximum 1-2 lines only.
    Don't repeat the same lines. 
    Don't complete the story fully only next scene of the story with 1-2 lines only.
    Don't describe the scene too much with the person or weather current situation (For example do not use "quickened pace", do not use "heart pounding". do not use "Weather is clear", do not use "sunny day")
    """
    return SystemMessage(content=system_prompt)

def start_story_node(state: State) -> State:
    state["story"] = [system_prompt()] + state["story"]

    result = llm.invoke(state["story"])
    return {"story": [result], "control": "ai_done"}

def continue_story_node(state: State) -> State:
    messages_with_system = [system_prompt()] + state["story"]
    result = llm.invoke(messages_with_system)
    return {"story": [result], "control": "ai_done"}

def user_input_node(state: State) -> State:
    print("\n" + "="*50)
    print("Current story:")
    for message in state["story"]:
        if isinstance(message, HumanMessage):
            print(f"User: {message.content}")
        elif isinstance(message, AIMessage):
            print(f"AI: {message.content}")
    print("="*50)
    
    user_input = input("\nAdd your next lines to the story (or type 'end' to finish): ")
    
    if user_input.lower().strip() == 'end':
        return {"story": state["story"], "control": "end"}
    else:
        return {"story": [HumanMessage(content=user_input)], "control": "user_done"}

def should_continue(state: State) -> str:
    if state["control"] == "end":
        return "end"
    elif state["control"] == "ai_done":
        return "user_input"
    elif state["control"] == "user_done":
        return "continue_story"
    else:
        return "continue_story"

graph_builder = StateGraph(State)
graph_builder.add_node("start_story", start_story_node)
graph_builder.add_node("continue_story", continue_story_node)
graph_builder.add_node("user_input", user_input_node)

graph_builder.add_edge(START, "start_story")
graph_builder.add_conditional_edges("start_story", should_continue)
graph_builder.add_conditional_edges("continue_story", should_continue)
graph_builder.add_conditional_edges("user_input", should_continue)

graph = graph_builder.compile()

if __name__ == "__main__":
    print("Welcome to the Interactive Story Assistant!")
    print("You'll start the story, then AI will add lines, then you can add more, and so on.")
    print("Type 'end' when you want to finish the story.\n")
    
    initial_story = input("Start your story: ")
    
    result = graph.invoke({
        "story": [
            HumanMessage(content=initial_story)
        ],
        "control": "start"
    })
    
    print("\n" + "="*50)
    print("FINAL STORY:")
    print("="*50)
    for message in result["story"]:
        if isinstance(message, HumanMessage):
            print(f"User: {message.content}")
        elif isinstance(message, AIMessage):
            print(f"AI: {message.content}")
    print("="*50)
    print("Story completed!")
