from Features.pytube_downloader import download_with_pytube
from config import DOWNLOADS_DIR

if __name__ == "__main__":
    # Define YouTube video URL
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your video URL

    # Start the download process
    download_with_pytube(video_url, DOWNLOADS_DIR)