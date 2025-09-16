import logging
from pathlib import Path
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import json, os

# --- Импортируем свои модули ---
from main import download_video, extract_audio, transcribe_audio, generate_summary
from make_presentation import generate_presentation  # функция для генерации презентации через SlidesGPT

API_TOKEN = "7601793959:AAH0bRefVi1q2Ys4n7PBWFsf5RyHxauCaGs"
BASE_OUTPUT = Path("output")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! Send me a YouTube link or a video file, and I'll turn it into an AI-generated presentation."
    )

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    url = msg.text if msg.text else None
    user_id = msg.from_user.id

    if not url:
        await msg.reply_text("❌ Please send a YouTube link for processing.")
        return

    await msg.reply_text("Processing your video, please wait... ⏳")

    try:
        # --- Папка сессии пользователя ---
        session_folder = BASE_OUTPUT / f"session_{user_id}"
        session_folder.mkdir(parents=True, exist_ok=True)
        summary_file = session_folder / "summary.json"
        transcript_file = session_folder / "transcript.json"
        output_pptx = session_folder / "slidesgpt_presentation.pptx"

        # --- Шаг 1: скачать видео и извлечь аудио ---
        video_path = download_video(url)
        audio_path = extract_audio(video_path)

        # --- Шаг 2: транскрипция ---
        segments = transcribe_audio(audio_path)
        with open(transcript_file, "w", encoding="utf-8") as f:
            json.dump(segments, f, ensure_ascii=False, indent=2)

        # --- Шаг 3: резюме ---
        summary_text = generate_summary(transcript_file=transcript_file)
        with open(summary_file, "w", encoding="utf-8") as f:
            json.dump(summary_text, f, ensure_ascii=False, indent=2)

        # --- Шаг 4: презентация через SlidesGPT ---
        generate_presentation(str(summary_file), str(transcript_file), str(output_pptx))

        # --- Шаг 5: отправка презентации пользователю ---
        if output_pptx.exists():
            await msg.reply_document(document=open(output_pptx, "rb"))
        else:
            await msg.reply_text("❌ Presentation was not created.")

    except Exception as e:
        await msg.reply_text(f"❌ Error: {e}")

# --- Основной запуск бота ---
if __name__ == "__main__":
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_video))

    print("Bot is running...")
    app.run_polling()
