import yt_dlp


def fetch_info(url: str):
    """
    Fetch video information without downloading.
    Returns cleaned metadata + filtered formats list.
    """

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    # Filter only video formats with resolution
    formats = []
    for f in info.get("formats", []):
        if (
            f.get("height") and
            f.get("ext") in ["mp4", "mkv", "webm"] and
            f.get("vcodec") != "none"
        ):
            formats.append({
                "format_id": f.get("format_id"),
                "height": f.get("height"),
                "ext": f.get("ext"),
                "filesize": f.get("filesize"),
            })

    return {
        "title": info.get("title"),
        "duration": info.get("duration"),
        "thumbnail": info.get("thumbnail"),
        "tags": info.get("tags", []),
        "formats": formats
    }
