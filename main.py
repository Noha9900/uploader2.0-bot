# ==========================================
# SUPER MIRROR BOT - MAIN ENTRY
# ==========================================

import asyncio
import logging
from pyrogram import Client
from config import BOTS, API_ID, API_HASH
from core.bot_manager import register


# =========================
# LOGGING SETUP
# =========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# =========================
# START SINGLE BOT
# =========================
async def start_bot(bot_data):
    """
    Starts a single bot instance
    """

    app = Client(
        name=bot_data.get("BOT_NAME", "mirror_bot"),
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=bot_data["BOT_TOKEN"],
        workers=20,
        in_memory=True  # IMPORTANT for Render
    )

    await app.start()

    # Register handlers
    register(app, bot_data)

    logger.info(f"✅ Bot started: {bot_data.get('BOT_NAME')}")

    return app


# =========================
# START ALL BOTS
# =========================
async def main():
    apps = []

    for bot_data in BOTS:
        try:
            app = await start_bot(bot_data)
            apps.append(app)
        except Exception as e:
            logger.error(f"❌ Failed to start bot: {e}")

    if not apps:
        logger.error("❌ No bots started. Exiting...")
        return

    logger.info("🚀 All bots initialized successfully!")

    # Keep running forever
    await asyncio.Event().wait()


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped manually.")
