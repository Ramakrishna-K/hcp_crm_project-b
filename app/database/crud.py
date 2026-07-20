import json

from sqlalchemy.orm import Session

from app.database.models import Interaction


def create_interaction(db: Session, data: dict):

    interaction = Interaction(

        hcp_name=data["hcp_name"],
        interaction_type=data["interaction_type"],
        date=data["date"],
        time=data["time"],

        attendees=json.dumps(data["attendees"]),
        topics=json.dumps(data["topics"]),
        materials=json.dumps(data["materials"]),
        samples=json.dumps(data["samples"]),

        sentiment=data["sentiment"],

        outcomes=data["outcomes"],
        follow_up=data["follow_up"],

        summary=data["summary"],
        next_action=data["next_action"]
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


def get_all_interactions(db: Session):

    return db.query(Interaction).all()


def get_interaction(db: Session, interaction_id: int):

    return db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()


def delete_interaction(db: Session, interaction_id: int):

    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if interaction:
        db.delete(interaction)
        db.commit()

    return interaction