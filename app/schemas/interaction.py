
from pydantic import BaseModel, Field
from typing import Optional, List

# AI Chat Request

class InteractionRequest(BaseModel):
    message: str


# Save Interaction Request

class InteractionCreate(BaseModel):
    hcp_name: Optional[str] = None
    interaction_type: Optional[str] = None

    date: Optional[str] = None
    time: Optional[str] = None

    attendees: List[str] = Field(default_factory=list)
    topics: List[str] = Field(default_factory=list)
    materials: List[str] = Field(default_factory=list)
    samples: List[str] = Field(default_factory=list)

    sentiment: Optional[str] = None
    outcomes: Optional[str] = None
    follow_up: Optional[str] = None

    summary: Optional[str] = None
    next_action: Optional[str] = None


# AI Response

class InteractionResponse(BaseModel):
    hcp_name: Optional[str] = None
    interaction_type: Optional[str] = None

    date: Optional[str] = None
    time: Optional[str] = None

    attendees: List[str] = Field(default_factory=list)
    topics: List[str] = Field(default_factory=list)
    materials: List[str] = Field(default_factory=list)
    samples: List[str] = Field(default_factory=list)

    sentiment: Optional[str] = None
    outcomes: Optional[str] = None
    follow_up: Optional[str] = None

    summary: Optional[str] = None
    next_action: Optional[str] = None