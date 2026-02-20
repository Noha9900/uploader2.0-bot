import os
import asyncio
from config import DOWNLOAD_PATH
from modules.downloader import link_handler


async def text_file_handler(client, message, bot_data):
    """
    Handles uploaded .txt file containing links.
    Each line should contain one URL.
    """

    status = await message.reply("📄 Reading text file...")

    os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    # Download file
    file_path = await message.download(file_name=DOWNLOAD_PATH)

    try:
        # Read links
        with open(file_path, "r", encoding="utf-8") as f:
            links = [line.strip() for line in f if line.strip()]

    except Exception as e:
        os.remove(file_path)
        return await status.edit(f"❌ Failed to read file.\nError: {e}")

    # Remove file after reading
    os.remove(file_path)

    if not links:
        return await status.edit("❌ No valid links found inside file.")

    await status.edit(
        f"🔗 Found **{len(links)}** links.\n\n🚀 Starting processing..."
    )

    success = 0
    failed = 0

    for link in links:
        try:
            # Create a fake message-like object safely
            message.text = link
            await link_handler(client, message, bot_data)
            success += 1

            # small delay to prevent flood
            await asyncio.sleep(2)

        except Exception as e:
            failed += 1
            await status.edit(
                f"⚠️ Error while processing:\n{link}\n\n{e}"
            )
            await asyncio.sleep(2)

    await status.edit(
        f"🎉 Processing Complete!\n\n"
        f"✅ Success: {success}\n"
        f"❌ Failed: {failed}"
    )
