
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
