import yt_dlp

def fetch_info(url):
    with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title"),
        "tags": info.get("tags", []),
        "formats": info.get("formats", [])
    }
