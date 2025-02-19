from pytube import YouTube
from moviepy.editor import AudioFileClip

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your video URL

# Create a YouTube object
yt = YouTube(video_url)

# Get the audio stream (highest quality)
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio
output_file = audio_stream.download(output_path=".", filename="audio")  # Saves as "audio.mp4"
print(f"Downloaded audio to: {output_file}")

# Convert to MP3
mp3_file = "audio.mp3"
audio_clip = AudioFileClip(output_file)
audio_clip.write_audiofile(mp3_file)
audio_clip.close()

print(f"Converted audio to: {mp3_file}")