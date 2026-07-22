
from fastapi import APIRouter, HTTPException
from app.schemas.interaction import InteractionCreate
import app.database.db as database

router = APIRouter(
    prefix="/interaction",
    tags=["Interaction"]
)


@router.post("/")
async def create_interaction(data: InteractionCreate):
    try:

        if database.interaction_collection is None:
            raise HTTPException(
                status_code=500,
                detail="MongoDB is not connected"
            )

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
            "next_action": data.next_action,
        }

        # print("========== INSERT ==========")
        # print(interaction)

        result = await database.interaction_collection.insert_one(interaction)

        inserted_document = await database.interaction_collection.find_one(
            {"_id": result.inserted_id}
        )

        inserted_document["_id"] = str(inserted_document["_id"])

        return {
            "success": True,
            "message": "Interaction saved successfully",
            "data": inserted_document
        }

    except HTTPException:
        raise

    except Exception as e:
        import traceback
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )