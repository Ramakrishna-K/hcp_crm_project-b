



from langgraph.graph import StateGraph, END

from app.agent.state import AgentState
from app.agent.nodes import (
    extract_node,
    summarize_node,
    recommendation_node
)

builder = StateGraph(AgentState)

builder.add_node("extract", extract_node)
builder.add_node("summarize", summarize_node)
builder.add_node("recommend", recommendation_node)

builder.set_entry_point("extract")

builder.add_edge("extract", "summarize")
builder.add_edge("summarize", "recommend")
builder.add_edge("recommend", END)

graph = builder.compile()


def run_agent(message: str):

    return graph.invoke({
        "message": message,

        "hcp_name": "",
        "interaction_type": "",
        "date": "",
        "time": "",
        "attendees": [],
        "topics": [],
        "materials": [],
        "samples": [],
        "outcomes": "",
        "follow_up": "",

        "summary": "",
        "next_action": "",
        "sentiment": ""
    })