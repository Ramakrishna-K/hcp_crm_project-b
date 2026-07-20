


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.database.db import engine, Base
from app.database.models import Interaction  # Import your model

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Sales Representative",
    description="FastAPI + LangGraph + Groq AI CRM Backend",
    version="1.0.0",
)

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all API routes
app.include_router(router)

# Home API
@app.get("/")
def home():
    return {
        "message": "AI Sales Representative API Running 🚀"
    }

# Run Server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )