from modules.rename import get_rename
from modules.thumbnail import get_thumbnail

async def upload(client, chat_id, file_path, user_id):

    new_name = get_rename(user_id)
    thumb = get_thumbnail(user_id)

    if new_name:
        import os
        ext = file_path.split(".")[-1]
        new_path = file_path.replace(file_path, f"{new_name}.{ext}")
        os.rename(file_path, new_path)
        file_path = new_path

    await client.send_video(
        chat_id,
        video=file_path,
        thumb=thumb
    )
