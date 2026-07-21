

# from sqlalchemy import create_engine ,text
# from sqlalchemy.orm import declarative_base, sessionmaker

# from app.config import settings

# engine = create_engine(
#     settings.DATABASE_URL,
#     pool_pre_ping=True
# )

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()

# try:
#     with engine.connect() as connection:
#         connection.execute(text("SELECT 1"))
#         print("      MySQL Database Connected Successfully")

# except Exception as e:
#     print("       Database Connection Failed")
#     print(e)


# def get_db():

#     db = SessionLocal()

#     try:
#         yield db

#     finally:
#         db.close()
# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# from motor.motor_asyncio import AsyncIOMotorClient
# from app.config import settings

# # MongoDB Client
# client = AsyncIOMotorClient(settings.MONGODB_URL)

# # Database
# db = client["crm_hcp"]

# # Collections
# interaction_collection = db["interactions"]
# hcp_collection = db["hcps"]

# # Test Connection
# try:
#     print("🚀 Connecting to MongoDB Atlas...")

#     client.admin.command("ping")

#     print("✅ MongoDB Connected Successfully")

# except Exception as e:
#     print("❌ MongoDB Connection Failed")
#     print(e)


# from motor.motor_asyncio import AsyncIOMotorClient
# from app.config import settings

# client = None
# db = None
# interaction_collection = None
# hcp_collection = None


# async def connect_to_mongo():
#     global client, db, interaction_collection, hcp_collection

#     client = AsyncIOMotorClient(settings.MONGODB_URL)

#     # Test connection
#     await client.admin.command("ping")
#     print("✅ MongoDB Connected Successfully")

#     db = client["crm_hcp"]

#     interaction_collection = db["interactions"]
#     hcp_collection = db["hcps"]


# async def close_mongo_connection():
#     global client

#     if client:
#         client.close()
#         print("🔴 MongoDB Connection Closed")



from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv


load_dotenv()


client = None
db = None


async def connect_to_mongo():

    global client, db

    client = AsyncIOMotorClient(
        os.getenv("MONGO_URL")
    )

    db = client["crm_hcp"]

    print("✅ MongoDB Atlas Connected")



async def close_mongo_connection():

    global client

    if client:
        client.close()



def get_collection():

    return db["interactions"]