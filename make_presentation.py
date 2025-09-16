import json
import requests
import os
from pathlib import Path

API_KEY = "15h8wsms06569n7n2qqhns9gezjxafbe"

def generate_presentation(summary_path: str, transcript_path: str, output_path: str):
    """
    Генерирует презентацию через SlidesGPT по файлам summary.json и transcript.json
    """
    # Проверяем файлы
    if not os.path.exists(summary_path) or not os.path.exists(transcript_path):
        raise FileNotFoundError("summary.json или transcript.json не найдены")

    # Загружаем контент
    with open(summary_path, "r", encoding="utf-8") as f:
        summary_text = json.load(f)
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript_text = json.load(f)

    # Формируем промпт
    prompt = f"""
Create a professional and visually appealing presentation based on the following content.
Use the summary to generate slide titles and key points.
Use the transcript to enrich slides with important details, but avoid too much text on one slide.
Add images, stylish backgrounds, and proper formatting for each slide. Make the presentation professional and beautiful.
Summary: {summary_text}
Transcript: {transcript_text}
"""

    url = "https://api.slidesgpt.com/v1/presentations/generate"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"prompt": prompt}

    # Отправляем запрос
    response = requests.post(url, headers=headers, json=data, timeout=60)
    response.raise_for_status()
    result = response.json()

    download_url = result.get("download")
    if not download_url:
        raise ValueError("Не удалось получить ссылку на презентацию")

    # Скачиваем готовую презентацию
    r = requests.get(download_url, timeout=60)
    r.raise_for_status()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(r.content)

    return Path(output_path)
