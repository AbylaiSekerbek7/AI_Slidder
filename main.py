from downloader import download_video
from audio_extract import extract_audio
from stt import transcribe_audio
import json
import os
from summarize import generate_summary

if __name__ == "__main__":
    url = "https://youtu.be/b-Pn0yXL9y8?si=ddj2MOw-Ccfqk2Tx"
    
    # Скачиваем видео
    video_path = download_video(url)
    print("Видео скачано:", video_path)

    # Извлекаем аудио
    audio_path = extract_audio(video_path)
    print("Аудио сохранено:", audio_path)

    # Транскрибируем аудио
    segments = transcribe_audio(audio_path)
    print("⏳ Распознаем речь...")

    # Выводим транскрипт с таймкодами в консоль
    for seg in segments:
        print(f"[{seg['start']:.2f}s - {seg['end']:.2f}s] {seg['text']}")

    # Сохраняем транскрипт в JSON
    os.makedirs("output", exist_ok=True)
    transcript_file = os.path.join("output", "transcript.json")
    with open(transcript_file, "w", encoding="utf-8") as f:
        json.dump(segments, f, ensure_ascii=False, indent=2)

    print(f"Транскрипт сохранён в {transcript_file}")

    summary_text = generate_summary(transcript_file=transcript_file)
    print("Резюме подкаста:\n", summary_text)