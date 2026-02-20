import yt_dlp
import os
from config import DOWNLOAD_PATH

async def download(url, format_id):

    ydl_opts = {
        "format": format_id,
        "outtmpl": f"{DOWNLOAD_PATH}/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        file_path = ydl.prepare_filename(info)

    return file_path
