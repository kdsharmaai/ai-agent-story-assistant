from langgraph.graph import StateGraph, START
from nodes import State, start_story_node, continue_story_node, should_continue

def create_web_story_graph():
    """Create and return the compiled story graph for web interface"""
    graph_builder = StateGraph(State)
    graph_builder.add_node("start_story", start_story_node)
    graph_builder.add_node("continue_story", continue_story_node)

    graph_builder.add_edge(START, "start_story")
    graph_builder.add_conditional_edges("start_story", should_continue)
    graph_builder.add_conditional_edges("continue_story", should_continue)

    graph = graph_builder.compile()

    return graph

# Create the web graph instance
web_graph = create_web_story_graph() 