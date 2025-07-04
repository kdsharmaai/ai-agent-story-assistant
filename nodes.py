from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    story: Annotated[list, add_messages]
    control: str

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)

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
    """Start story node for web interface"""
    state["story"] = [system_prompt()] + state["story"]
    result = llm.invoke(state["story"])
    return {"story": [result], "control": "end"}

def continue_story_node(state: State) -> State:
    """Continue story node for web interface"""
    messages_with_system = [system_prompt()] + state["story"]
    result = llm.invoke(messages_with_system)
    return {"story": [result], "control": "end"}

def should_continue(state: State) -> str:
    """Simplified control flow for web interface"""
    if state["control"] == "end":
        return "end"
    elif state["control"] == "start":
        return "start_story"
    elif state["control"] == "user_done":
        return "continue_story"
    else:
        return "continue_story" 