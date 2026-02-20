# ==========================================
# SUPER MIRROR BOT - FINAL PRODUCTION CONFIG
# ==========================================

import os
import json

# =========================
# TELEGRAM API
# =========================
API_ID = int(os.getenv("API_ID", "36982189"))
API_HASH = os.getenv("API_HASH", "d3ec5feee7342b692e7b5370fb9c8db7")

if not API_ID or not API_HASH:
    raise ValueError("API_ID or API_HASH is missing.")


# =========================
# GLOBAL SETTINGS
# =========================
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "/tmp")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"


# =========================
# PERFORMANCE SETTINGS
# =========================
MAX_CONCURRENT_DOWNLOADS = int(os.getenv("MAX_CONCURRENT_DOWNLOADS", "5"))
MAX_CONCURRENT_UPLOADS = int(os.getenv("MAX_CONCURRENT_UPLOADS", "3"))
PROGRESS_UPDATE_INTERVAL = int(os.getenv("PROGRESS_UPDATE_INTERVAL", "3"))


# =========================
# FILE LIMIT
# =========================
MAX_FILE_SIZE = int(os.getenv(
    "MAX_FILE_SIZE",
    str(2 * 1024 * 1024 * 1024)
))


# =========================
# REDIS (OPTIONAL)
# =========================
USE_REDIS = os.getenv("USE_REDIS", "False").lower() == "true"
REDIS_URL = os.getenv("REDIS_URL", "")


# =========================
# MULTI BOT CONFIG
# =========================
try:
    BOTS = json.loads(os.getenv("BOTS", "[]"))
except Exception:
    raise ValueError("BOTS must be valid JSON.")

if not BOTS:
    raise ValueError("BOTS is missing in Render Environment Variables.")

required_keys = ["BOT_TOKEN", "OWNER_ID", "MONGO_URI"]

for key in required_keys:
    if key not in BOTS[0]:
        raise ValueError(f"BOTS is missing required key: {key}")
