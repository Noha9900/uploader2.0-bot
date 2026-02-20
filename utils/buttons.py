from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def resolution_buttons(formats: list):
    """
    Generate resolution selection inline buttons
    formats = yt-dlp extracted formats list
    """

    buttons = []
    added = set()  # avoid duplicate resolutions

    # Sort formats by height (highest first)
    sorted_formats = sorted(
        formats,
        key=lambda x: x.get("height") or 0,
        reverse=True
    )

    for f in sorted_formats:
        height = f.get("height")
        format_id = f.get("format_id")

        if not height or not format_id:
            continue

        # Skip duplicates like multiple 720p entries
        if height in added:
            continue

        added.add(height)

        buttons.append([
            InlineKeyboardButton(
                text=f"{height}p",
                callback_data=f"res|{format_id}"
            )
        ])

    # Add cancel button
    buttons.append([
        InlineKeyboardButton("❌ Cancel", callback_data="cancel")
    ])

    return InlineKeyboardMarkup(buttons)
