

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.interaction import InteractionCreate
from app.database.db import get_db
from app.database.models import Interaction

router = APIRouter(
    prefix="/interaction",
    tags=["Interaction"]
)


@router.post("")
def create_interaction(
    data: InteractionCreate,
    db: Session = Depends(get_db)
):

    interaction = Interaction(
        hcp_name=data.hcp_name,
        interaction_type=data.interaction_type,
        date=data.date,
        time=data.time,
        attendees=",".join(data.attendees),
        topics=",".join(data.topics),
        materials=",".join(data.materials),
        samples=",".join(data.samples),
        sentiment=data.sentiment,
        outcomes=data.outcomes,
        follow_up=data.follow_up,
        summary=data.summary,
        next_action=data.next_action,
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {
        "success": True,
        "message": "Interaction saved successfully",
        "id": interaction.id
    }