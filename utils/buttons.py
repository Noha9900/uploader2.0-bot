from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def resolution_buttons(formats):
    btn = []
    for f in formats:
        if f.get("height"):
            btn.append([
                InlineKeyboardButton(
                    f"{f['height']}p",
                    callback_data=f"res|{f['format_id']}"
                )
            ])
    return InlineKeyboardMarkup(btn)
