from pyrogram import filters
from pyrogram.types import Message

from modules.welcome import welcome_handler
from modules.rename import set_rename
from modules.textfile import text_file_handler
from modules.downloader import link_handler
from modules.thumbnail import set_thumbnail, delete_thumbnail

# Temporary state to know user is setting thumbnail
waiting_for_thumb = set()


def register(app, bot_data):

    # ===============================
    # START COMMAND
    # ===============================
    @app.on_message(filters.command("start"))
    async def start_handler(client, message: Message):
        await welcome_handler(client, message)

    # ===============================
    # RENAME COMMAND
    # Usage: /rename new_name
    # ===============================
    @app.on_message(filters.command("rename"))
    async def rename_handler(client, message: Message):
        if len(message.command) < 2:
            return await message.reply(
                "❌ Usage:\n`/rename New_File_Name`"
            )

        new_name = message.text.split(" ", 1)[1].strip()
        await set_rename(message.from_user.id, new_name)

        await message.reply(
            f"✅ Rename set to:\n`{new_name}`"
        )

    # ===============================
    # SET THUMBNAIL COMMAND
    # ===============================
    @app.on_message(filters.command("setthumb"))
    async def set_thumb_command(client, message: Message):
        waiting_for_thumb.add(message.from_user.id)
        await message.reply("📸 Please send the photo you want to set as thumbnail.")

    # ===============================
    # DELETE THUMBNAIL COMMAND
    # ===============================
    @app.on_message(filters.command("delthumb"))
    async def del_thumb_command(client, message: Message):
        await delete_thumbnail(message.from_user.id)
        await message.reply("🗑️ Thumbnail deleted successfully.")

    # ===============================
    # PHOTO HANDLER (For Thumbnail)
    # ===============================
    @app.on_message(filters.photo)
    async def thumbnail_handler(client, message: Message):
        user_id = message.from_user.id

        if user_id not in waiting_for_thumb:
            return  # Ignore normal photos

        waiting_for_thumb.remove(user_id)

        file_id = message.photo.file_id
        await set_thumbnail(user_id, file_id)

        await message.reply("✅ Thumbnail saved successfully!")

    # ===============================
    # TEXT FILE UPLOADER (.txt)
    # ===============================
    @app.on_message(filters.document)
    async def text_upload_handler(client, message: Message):

        if not message.document.file_name.endswith(".txt"):
            return

        await text_file_handler(client, message, bot_data)

    # ===============================
    # LINK HANDLER (Single Link)
    # ===============================
    @app.on_message(filters.text & ~filters.command([
        "start", "rename", "setthumb", "delthumb"
    ]))
    async def handle_links(client, message: Message):
        await link_handler(client, message, bot_data)
