from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def welcome_handler(client, message):
    text = """
👋 **Welcome to Super Mirror Bot**

🚀 **Features:**
• 🎬 Download YouTube & Public Videos  
• 📄 Upload from Text File  
• ✏️ Rename Before Upload  
• 📢 Auto Upload to Channel (if set)  

⚡ **Send any video link to get started!**
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📘 Help", callback_data="help"),
                InlineKeyboardButton("ℹ️ About", callback_data="about"),
            ],
            [
                InlineKeyboardButton("📢 Updates Channel", url="https://t.me/your_channel")
            ]
        ]
    )

    await message.reply(
        text,
        reply_markup=buttons,
        disable_web_page_preview=True
    )
