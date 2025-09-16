AI Video-to-Presentation Bot 🎬📊

Transform any video into professional AI-generated presentations in minutes!

🔹 Project Description

This project automates the creation of presentations from videos. It:

Downloads YouTube videos.

Extracts audio from the video.

Transcribes speech using Whisper.

Generates a concise summary of the content.

Creates visually appealing PowerPoint presentations via SlidesGPT API.

Integrates with Telegram: send a link and the bot returns a ready-made presentation.

Goal: Save time and automate the process of preparing presentations.

🔹 Features

Automatic video and audio processing.

Structured and visually appealing slide generation.

Telegram bot for easy interaction with video links.

Supports multiple users (after implementing unique temporary files).

🔹 Technologies Used

Python 3.11+

MoviePy – audio extraction from video

Whisper – speech transcription

OpenAI API – summary generation

SlidesGPT API – presentation creation

python-telegram-bot – Telegram bot integration

VS Code / PyCharm – development environment

🔹 Installation

Clone the repository,
Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows


Install dependencies:

pip install -r requirements.txt


Add your API keys:

Telegram Bot Token in bot/bot.py

SlidesGPT API Key in make_presentation.py

OpenAI API Key (if used for summary generation)

Run locally via Telegram bot

Start the bot:

python bot/bot.py


Send a YouTube video link in Telegram.

Receive the generated presentation as a reply.

Direct presentation generation without bot
python main.py
python make_presentation.py


Video and transcript are saved in output/.

Presentation is saved as output/slidesgpt_presentation.pptx.

🔹 License

MIT License © Sekerbek Abylaikhan & Sarsenov Amirlan
