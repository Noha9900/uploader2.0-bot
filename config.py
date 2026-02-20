# ==========================================
# SUPER MIRROR BOT - GLOBAL CONFIG (RENDER READY)
# ==========================================

import os
import json

# =========================
# TELEGRAM API
# =========================
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")


# =========================
# GLOBAL BOT SETTINGS
# =========================
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "/tmp")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"


# =========================
# QUEUE & PERFORMANCE
# =========================
MAX_CONCURRENT_DOWNLOADS = int(os.getenv("MAX_CONCURRENT_DOWNLOADS", 5))
MAX_CONCURRENT_UPLOADS = int(os.getenv("MAX_CONCURRENT_UPLOADS", 3))
PROGRESS_UPDATE_INTERVAL = int(os.getenv("PROGRESS_UPDATE_INTERVAL", 3))


# =========================
# FILE LIMITS
# =========================
MAX_FILE_SIZE = int(os.getenv(
    "MAX_FILE_SIZE",
    2 * 1024 * 1024 * 1024  # 2GB default
))


# =========================
# OPTIONAL REDIS
# =========================
USE_REDIS = os.getenv("USE_REDIS", "False").lower() == "true"
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")


# =========================
# MULTI BOT CONFIGURATION
# =========================
BOTS = json.loads(os.getenv("BOTS"))
