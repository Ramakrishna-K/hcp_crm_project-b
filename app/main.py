
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.database.db import (
    connect_to_mongo,
    close_mongo_connection,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    print(" Application Started")

    yield

    # Shutdown
    await close_mongo_connection()
    print(" Application Stopped")


app = FastAPI(
    title="AI Sales Representative",
    description="FastAPI + LangGraph + Groq AI CRM Backend",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://crm-project-f-engu.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def home():
    return {
        "success": True,
        "message": "AI Sales Representative API Running 🚀",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "database": "MongoDB Atlas",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
