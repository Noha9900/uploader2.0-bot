# ==========================================
# SUPER MIRROR BOT - GLOBAL CONFIG
# ==========================================


# =========================
# TELEGRAM API
# =========================
API_ID = 123456
API_HASH = "YOUR_API_HASH"


# =========================
# GLOBAL BOT SETTINGS
# =========================
DOWNLOAD_PATH = "./downloads"   # Use "/tmp" if deploying on Render
LOG_LEVEL = "INFO"
DEBUG = False


# =========================
# QUEUE & PERFORMANCE
# =========================
MAX_CONCURRENT_DOWNLOADS = 2
MAX_CONCURRENT_UPLOADS = 1
PROGRESS_UPDATE_INTERVAL = 3   # seconds


# =========================
# FILE LIMITS
# =========================
# Telegram Bot API limit = 2GB
# Telegram Premium userbot = 4GB
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024   # 2GB


# =========================
# OPTIONAL REDIS (Future Upgrade)
# =========================
USE_REDIS = False
REDIS_URL = "redis://localhost:6379"


# =========================
# MULTI BOT CONFIGURATION
# Add unlimited bots here
# =========================
BOTS = [

    # =========================
    # BOT 1
    # =========================
    {
        "BOT_NAME": "SuperMirrorBot1",

        "BOT_TOKEN": "BOT_TOKEN_1",

        # Mongo database for this bot
        "MONGO_URI": "mongodb+srv://user:pass@cluster/db1",

        # Admin users (full control)
        "ADMIN_IDS": [123456789],

        # If None → Upload to user chat
        # If set → Upload directly to this channel
        "CHANNEL_ID": None,

        # Allow public usage?
        "PUBLIC_MODE": True
    },


    # =========================
    # BOT 2
    # =========================
    {
        "BOT_NAME": "SuperMirrorBot2",

        "BOT_TOKEN": "BOT_TOKEN_2",

        "MONGO_URI": "mongodb+srv://user:pass@cluster/db2",

        "ADMIN_IDS": [987654321],

        # Example channel ID
        "CHANNEL_ID": -1001234567xxx,

        "PUBLIC_MODE": False
    }

]
