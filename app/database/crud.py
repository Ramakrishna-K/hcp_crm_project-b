# import json

# from sqlalchemy.orm import Session

# from app.database.models import Interaction


# def create_interaction(db: Session, data: dict):

#     interaction = Interaction(

#         hcp_name=data["hcp_name"],
#         interaction_type=data["interaction_type"],
#         date=data["date"],
#         time=data["time"],

#         attendees=json.dumps(data["attendees"]),
#         topics=json.dumps(data["topics"]),
#         materials=json.dumps(data["materials"]),
#         samples=json.dumps(data["samples"]),

#         sentiment=data["sentiment"],

#         outcomes=data["outcomes"],
#         follow_up=data["follow_up"],

#         summary=data["summary"],
#         next_action=data["next_action"]
#     )

#     db.add(interaction)
#     db.commit()
#     db.refresh(interaction)

#     return interaction


# def get_all_interactions(db: Session):

#     return db.query(Interaction).all()


# def get_interaction(db: Session, interaction_id: int):

#     return db.query(Interaction).filter(
#         Interaction.id == interaction_id
#     ).first()


# def delete_interaction(db: Session, interaction_id: int):

#     interaction = db.query(Interaction).filter(
#         Interaction.id == interaction_id
#     ).first()

#     if interaction:
#         db.delete(interaction)
#         db.commit()

#     return interaction



from bson import ObjectId
import app.database.db as database


async def create_interaction(data: dict):

    result = await database.interaction_collection.insert_one(data)

    data["id"] = str(result.inserted_id)

    return data


async def get_all_interactions():

    interactions = []

    async for interaction in database.interaction_collection.find():

        interaction["id"] = str(interaction["_id"])
        del interaction["_id"]

        interactions.append(interaction)

    return interactions


async def get_interaction(interaction_id: str):

    interaction = await database.interaction_collection.find_one(
        {"_id": ObjectId(interaction_id)}
    )

    if interaction:
        interaction["id"] = str(interaction["_id"])
        del interaction["_id"]

    return interaction


async def delete_interaction(interaction_id: str):

    result = await database.interaction_collection.delete_one(
        {"_id": ObjectId(interaction_id)}
    )

    return result.deleted_count > 0