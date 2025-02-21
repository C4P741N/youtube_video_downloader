from pytube import YouTube
from moviepy import AudioFileClip
import yt_dlp
import os

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your video URL

# Ensure 'downloads' directory exists
downloads_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(downloads_dir, exist_ok=True)

def download_with_pytube(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Get the audio stream (highest quality)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio to 'downloads' folder
        output_file = audio_stream.download(output_path=downloads_dir, filename="audio")  # Saves as "audio.mp4"
        print(f"Downloaded audio using pytube to: {output_file}")

        # Convert to MP3
        mp3_file = os.path.join(downloads_dir, "audio.mp3")
        audio_clip = AudioFileClip(output_file)
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()

        print(f"Converted audio to: {mp3_file}")
    except Exception as e:
        print(f"Pytube failed with error: {e}")
        print("Trying yt_dlp...")

        # Fallback to yt_dlp if pytube fails
        download_with_yt_dlp(url)

def download_with_yt_dlp(url):
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

# Start the download process
download_with_pytube(video_url)