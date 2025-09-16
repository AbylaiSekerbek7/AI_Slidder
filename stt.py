# stt.py
import whisper

def transcribe_audio(file_path: str):
    model = whisper.load_model("small")  # лучше medium/large для точности
    result = model.transcribe(file_path)
    
    # Формируем красивый список сегментов с таймкодами
    segments = []
    for segment in result["segments"]:
        segments.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"].strip()
        })
    
    return segments
