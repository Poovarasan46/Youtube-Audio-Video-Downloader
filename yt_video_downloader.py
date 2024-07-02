#yt = YouTube('https://youtu.be/rzmU8ZY5ODI?si=fdB_pLDQWkpJLB0n',on_progress_callback=)
from pytube import YouTube
from tqdm import tqdm

# Callback function to update progress bar
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    progress_bar.update(len(chunk))
    progress_bar.set_postfix(percent=f'{percent:.2f}%')

# Callback function when download completes
def on_complete(stream, file_path):
    progress_bar.close()
    print(f"Download completed: {file_path}")

# YouTube video URL
url = 'https://youtu.be/rzmU8ZY5ODI?si=fdB_pLDQWkpJLB0n'

# Initialize YouTube object
yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)

# Select the stream (e.g., the first stream)
stream = yt.streams.first()

# Initialize progress bar
progress_bar = tqdm(total=stream.filesize, unit='B', unit_scale=True, desc='Downloading')

# Start download
stream.download()

# Final statement to ensure the script closes properly
print("Download finished successfully.")
