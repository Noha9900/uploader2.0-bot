from motor.motor_asyncio import AsyncIOMotorClient
from config import BOTS

# Use first bot's Mongo URI (or modify if multi-db)
MONGO_URI = BOTS[0]["MONGO_URI"]

client = AsyncIOMotorClient(MONGO_URI)
db = client["bot_data"]
rename_collection = db["user_rename"]


async def set_rename(user_id: int, name: str):
    """
    Save rename preference in MongoDB
    """
    await rename_collection.update_one(
        {"user_id": user_id},
        {"$set": {"rename": name}},
        upsert=True
    )


async def get_rename(user_id: int):
    """
    Get rename preference from MongoDB
    """
    data = await rename_collection.find_one({"user_id": user_id})
    if data:
        return data.get("rename")
    return None
