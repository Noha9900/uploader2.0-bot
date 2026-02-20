import yt_dlp
import os
import asyncio
from config import DOWNLOAD_PATH


async def download(url: str, format_id: str):
    """
    Downloads a video using yt-dlp without blocking the event loop.
    Returns downloaded file path.
    """

    os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    ydl_opts = {
        "format": format_id,
        "outtmpl": os.path.join(DOWNLOAD_PATH, "%(title).100s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "merge_output_format": "mp4",  # safer for Telegram upload
    }

    loop = asyncio.get_running_loop()

    def run_download():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)

    file_path = await loop.run_in_executor(None, run_download)

    return file_path
