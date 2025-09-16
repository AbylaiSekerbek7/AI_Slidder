from transformers import pipeline
import json

def generate_summary(transcript_file="output/transcript.json", output_file="output/summary.json"):
    # Загружаем summarization pipeline (бесплатная модель)
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Загружаем транскрипт
    with open(transcript_file, "r", encoding="utf-8") as f:
        segments = json.load(f)

    # Собираем весь текст
    full_text = " ".join([seg["text"] for seg in segments])

    # Разбиваем на части, чтобы не превышать ограничение модели
    max_chunk = 1000
    chunks = [full_text[i:i+max_chunk] for i in range(0, len(full_text), max_chunk)]

    # Генерируем резюме для каждой части и объединяем
    summary = ""
    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
        summary += result[0]['summary_text'] + " "

    # Сохраняем резюме в JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"Резюме сохранено в {output_file}")
    return summary