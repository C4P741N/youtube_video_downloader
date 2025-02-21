import yt_dlp
import os

def download_with_yt_dlp(url, downloads_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(downloads_dir, 'audio.%(ext)s'),  # Save to 'downloads' folder
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Downloaded and converted audio using yt_dlp.")
    except Exception as e:
        print(f"yt_dlp also failed with error: {e}")