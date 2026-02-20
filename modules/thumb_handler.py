from pyrogram import filters
from modules.thumbnail import set_thumbnail


async def thumbnail_handler(client, message):
    user_id = message.from_user.id

    if not message.photo:
        return await message.reply("❌ Please send a photo.")

    file_id = message.photo.file_id

    await set_thumbnail(user_id, file_id)

    await message.reply("✅ Thumbnail saved successfully!")
