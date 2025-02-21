from Features.yt_dlp_downloader import download_with_yt_dlp
from pytube import YouTube
from moviepy import AudioFileClip
import os


def download_with_pytube(url, downloads_dir):
    try:
        downloads_dir = os.path.join(os.getcwd(), "downloads")
        os.makedirs(downloads_dir, exist_ok=True)

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
        download_with_yt_dlp(url, downloads_dir)