import asyncio
from config import MAX_DOWNLOAD, MAX_UPLOAD


# ==========================================
# DOWNLOAD QUEUE (Limits concurrent downloads)
# ==========================================
download_semaphore = asyncio.Semaphore(MAX_DOWNLOAD)


# ==========================================
# UPLOAD QUEUE (Limits concurrent uploads)
# ==========================================
upload_semaphore = asyncio.Semaphore(MAX_UPLOAD)


# ==========================================
# DOWNLOAD WRAPPER
# ==========================================
async def run_download(task_coro):
    """
    Wrap any download coroutine inside this.
    It will respect MAX_DOWNLOAD limit.
    """
    async with download_semaphore:
        return await task_coro


# ==========================================
# UPLOAD WRAPPER
# ==========================================
async def run_upload(task_coro):
    """
    Wrap any upload coroutine inside this.
    It will respect MAX_UPLOAD limit.
    """
    async with upload_semaphore:
        return await task_coro


# ==========================================
# QUEUE STATUS
# ==========================================
def queue_status():
    return {
        "max_download": MAX_DOWNLOAD,
        "max_upload": MAX_UPLOAD,
        "current_download": MAX_DOWNLOAD - download_semaphore._value,
        "current_upload": MAX_UPLOAD - upload_semaphore._value,
    }
