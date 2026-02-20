# core/bot_manager.py

from pyrogram import filters
from pyrogram.types import Message

from modules.welcome import welcome_handler
from modules.rename import set_rename
from modules.textfile import text_file_handler
from modules.downloader import link_handler


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

        new_name = message.text.split(" ", 1)[1]
        await set_rename(message.from_user.id, new_name)

        await message.reply(
            f"✅ Rename set to:\n`{new_name}`"
        )


    # ===============================
    # TEXT FILE UPLOADER (.txt)
    # ===============================
    @app.on_message(filters.document)
    async def text_upload_handler(client, message: Message):

        # Only allow .txt files
        if not message.document.file_name.endswith(".txt"):
            return

        await text_file_handler(client, message, bot_data)


    # ===============================
    # LINK HANDLER (Single Link)
    # ===============================
    @app.on_message(filters.text & ~filters.command(["start", "rename"]))
    async def handle_links(client, message: Message):
        await link_handler(client, message, bot_data)
