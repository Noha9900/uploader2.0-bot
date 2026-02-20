import os
from motor.motor_asyncio import AsyncIOMotorClient
from config import BOTS

MONGO_URI = BOTS[0]["MONGO_URI"]

client = AsyncIOMotorClient(MONGO_URI)
db = client["bot_data"]
thumb_collection = db["user_thumbnail"]

THUMB_PATH = "thumbnails"
os.makedirs(THUMB_PATH, exist_ok=True)


async def set_thumbnail(user_id: int, file_id: str):
    """
    Save thumbnail file_id in MongoDB
    """
    await thumb_collection.update_one(
        {"user_id": user_id},
        {"$set": {"file_id": file_id}},
        upsert=True
    )


async def get_thumbnail(user_id: int):
    """
    Get thumbnail file_id
    """
    data = await thumb_collection.find_one({"user_id": user_id})
    if data:
        return data.get("file_id")
    return None


async def delete_thumbnail(user_id: int):
    """
    Remove thumbnail
    """
    await thumb_collection.delete_one({"user_id": user_id})
