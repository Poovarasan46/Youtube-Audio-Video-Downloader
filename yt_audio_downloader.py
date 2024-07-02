import os
from pytube import YouTube

# Create a folder to store the downloaded audio files
download_folder = 'downloaded_songs'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)


# Function to download the audio of a YouTube video
def download_audio(url):
    try:
        yt = YouTube(url)
        # Get the best audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio file
        print(f"Downloading audio from: {yt.title}")
        audio_file_path = audio_stream.download(output_path=download_folder)

        print(f"Downloaded to: {audio_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# List of YouTube video URLs to download
video_urls = ['Youtube video link here']

# Download audio for each video URL
for url in video_urls:
    download_audio(url)
