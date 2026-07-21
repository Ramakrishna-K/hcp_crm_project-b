
# from fastapi import APIRouter

# from app.schemas.interaction import InteractionCreate
# import app.database.db as database

# router = APIRouter(
#     prefix="/interaction",
#     tags=["Interaction"]
# )

# @router.post("")
# async def create_interaction(data: InteractionCreate):

#     interaction = {
#         "hcp_name": data.hcp_name,
#         "interaction_type": data.interaction_type,
#         "date": data.date,
#         "time": data.time,

#         "attendees": data.attendees,
#         "topics": data.topics,
#         "materials": data.materials,
#         "samples": data.samples,

#         "sentiment": data.sentiment,
#         "outcomes": data.outcomes,
#         "follow_up": data.follow_up,

#         "summary": data.summary,
#         "next_action": data.next_action,
#     }

#     result = await database.interaction_collection.insert_one(interaction)

#     return {
#         "success": True,
#         "message": "Interaction saved successfully",
#         "id": str(result.inserted_id),
#     }


from fastapi import APIRouter, HTTPException

from app.schemas.interaction import InteractionCreate
import app.database.db as database


router = APIRouter(
    prefix="/interaction",
    tags=["Interaction"]
)


@router.post("")
async def create_interaction(data: InteractionCreate):

    try:

        interaction = {
            "hcp_name": data.hcp_name,
            "interaction_type": data.interaction_type,

            "date": data.date,
            "time": data.time,

            "attendees": data.attendees,
            "topics": data.topics,
            "materials": data.materials,
            "samples": data.samples,

            "sentiment": data.sentiment,
            "outcomes": data.outcomes,
            "follow_up": data.follow_up,

            "summary": data.summary,
            "next_action": data.next_action
        }


        result = await database.interaction_collection.insert_one(
            interaction
        )


        return {
            "success": True,
            "message": "Interaction saved successfully",
            "id": str(result.inserted_id)
        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


