import os
from moviepy.editor import VideoFileClip

def extract_audio(video_path: str, output_folder="output") -> str:
    os.makedirs(output_folder, exist_ok=True)

    base = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_folder, base + ".mp3")

    # Берем аудиодорожку из видео
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    clip.close()

    return audio_path
