import os
from modules.rename import get_rename
from modules.thumbnail import get_thumbnail
from core.queue import run_upload


async def upload(client, chat_id, file_path, user_id):
    """
    Upload video with optional rename + thumbnail
    """

    try:
        # ===============================
        # GET USER SETTINGS (ASYNC)
        # ===============================
        new_name = await get_rename(user_id)
        thumb = await get_thumbnail(user_id)

        # ===============================
        # RENAME FILE IF USER SET NAME
        # ===============================
        if new_name:
            base_dir = os.path.dirname(file_path)
            ext = os.path.splitext(file_path)[1]
            new_path = os.path.join(base_dir, f"{new_name}{ext}")

            os.rename(file_path, new_path)
            file_path = new_path

        # ===============================
        # UPLOAD WITH QUEUE LIMIT
        # ===============================
        await run_upload(
            client.send_video(
                chat_id=chat_id,
                video=file_path,
                thumb=thumb,
                caption="🎬 Here is your video"
            )
        )

    finally:
        # ===============================
        # CLEANUP AFTER UPLOAD
        # ===============================
        if os.path.exists(file_path):
            os.remove(file_path)
