# main.py

import asyncio
from pyrogram import Client
from config import BOTS, API_ID, API_HASH
from core.bot_manager import register


async def start_bot(bot_data):
    """
    Starts a single bot instance
    """

    app = Client(
        name=f"bot_{bot_data['BOT_TOKEN'][:10]}",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=bot_data["BOT_TOKEN"],
        workers=10
    )

    # Start the bot
    await app.start()

    # Register all handlers for this bot
    register(app, bot_data)

    print(f"✅ Bot started: {bot_data['BOT_TOKEN'][:10]}...")

    return app


async def main():
    """
    Starts all bots defined in config.py
    """

    apps = []

    for data in BOTS:
        try:
            app = await start_bot(data)
            apps.append(app)
        except Exception as e:
            print(f"❌ Failed to start bot: {e}")

    print("🚀 All bots initialized successfully!")

    # Keep running forever
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
