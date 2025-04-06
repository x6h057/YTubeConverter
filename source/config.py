import source.api as api

folder = "temp"

config = {
    "mp3": {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            },
            {
                "key": "FFmpegMetadata",
            },
        ],
        "embedthumbnail": True,
        "prefer_ffmpeg": True,
        "keepvideo": False,
        "noplaylist": False,
        "quiet": False,
    },
    "mp4": {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
        "embedthumbnail": True,
        "merge_output_format": "mp4",
        "prefer_ffmpeg": True,
        "keepvideo": False,
        "noplaylist": False,
        "quiet": False,
    }
}