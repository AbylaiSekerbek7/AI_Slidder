import yt_dlp
import os

def download_video(url: str, output_path="output") -> str:
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'socket_timeout': 60
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info)
    return video_path