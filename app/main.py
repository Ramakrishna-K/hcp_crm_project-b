


# from contextlib import asynccontextmanager

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.api.routes import router
# from app.database.db import connect_to_mongo, close_mongo_connection


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup
#     await connect_to_mongo()

#     yield

#     # Shutdown
#     await close_mongo_connection()


# app = FastAPI(
#     title="AI Sales Representative",
#     description="FastAPI + LangGraph + Groq AI CRM Backend",
#     version="1.0.0",
#     lifespan=lifespan,
# )

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Register Routes
# app.include_router(router)


# @app.get("/")
# async def home():
#     return {
#         "success": True,
#         "message": "AI Sales Representative API Running 🚀"
#     }


# @app.get("/health")
# async def health():
#     return {
#         "status": "healthy",
#         "database": "MongoDB Atlas"
#     }


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(
#         "app.main:app",
#         host="127.0.0.1",
#         port=8000,
#         reload=True,
#     )



from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.database.db import (
    connect_to_mongo,
    close_mongo_connection
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Startup
    await connect_to_mongo()

    yield

    # Shutdown
    await close_mongo_connection()



app = FastAPI(
    title="AI Sales Representative",
    description="FastAPI + LangGraph + Groq AI CRM Backend",
    version="1.0.0",
    lifespan=lifespan
)



# CORS

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        # Add your frontend URL here after deployment
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)



# Register Routes

app.include_router(router)



@app.get("/")
async def home():

    return {
        "success": True,
        "message": "AI Sales Representative API Running 🚀"
    }



@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "database": "MongoDB Atlas"
    }



if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )