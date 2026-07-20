

from fastapi import APIRouter

from app.api.agent import router as agent_router
from app.api.interaction import router as interaction_router

router = APIRouter()

router.include_router(agent_router)
router.include_router(interaction_router)
