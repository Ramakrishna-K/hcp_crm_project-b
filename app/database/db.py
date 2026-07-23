

from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = None
db = None
interaction_collection = None


async def connect_to_mongo():
    global client, db, interaction_collection

    try:
        client = AsyncIOMotorClient(settings.MONGODB_URL)

        # Test MongoDB connection
        await client.admin.command("ping")

        db = client["crm_hcp"]
        interaction_collection = db["interactions"]

        print(" MongoDB Connected Successfully")
        # print("Database:", db.name)
        # print("Collection:", interaction_collection.name)

    except Exception as e:
        print("❌ MongoDB Connection Error:", e)
        raise


async def close_mongo_connection():
    global client

    if client:
        client.close()
        print("🔴 MongoDB Connection Closed")
