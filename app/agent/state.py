

from typing import TypedDict, List

class AgentState(TypedDict):
    message: str

    hcp_name: str
    interaction_type: str
    date: str
    time: str

    attendees: list[str]
    topics: list[str]
    materials: list[str]
    samples: list[str]

    sentiment: str
    outcomes: str
    follow_up: str

    summary: str
    next_action: str