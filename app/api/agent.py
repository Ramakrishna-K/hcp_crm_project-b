from fastapi import APIRouter, HTTPException
from app.schemas.interaction import InteractionRequest, InteractionResponse
from app.agent.graph import run_agent

router = APIRouter(
    prefix="/agent",
    tags=["AI Agent"],
)

@router.post("/chat", response_model=InteractionResponse)
def chat(request: InteractionRequest):
    try:
        result = run_agent(request.message)

        if not isinstance(result, dict):
            raise HTTPException(
                status_code=500,
                detail="run_agent() must return a dictionary.",
            )

        return InteractionResponse(
            hcp_name=result.get("hcp_name"),
            interaction_type=result.get("interaction_type"),
            date=result.get("date"),
            time=result.get("time"),
            attendees=result.get("attendees") or [],
            topics=result.get("topics") or [],
            materials=result.get("materials") or [],
            samples=result.get("samples") or [],
            sentiment=result.get("sentiment"),
            outcomes=result.get("outcomes"),
            follow_up=result.get("follow_up"),
            summary=result.get("summary"),
            next_action=result.get("next_action"),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
