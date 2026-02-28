from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from youtube_transcript_api import YouTubeTranscriptApi
import re
from openclaw_client import ask_openclaw
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
# memory
user_video_context = {}
user_language = {}
user_last_summary = {}


# -------------------------------
# Extract video ID
# -------------------------------
def extract_video_id(text):
    pattern = r"(?:v=|youtu\.be/|\/shorts\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, text)
    return match.group(1) if match else None


# -------------------------------
# Language detection
# -------------------------------
def detect_language(text):
    text = text.lower()
    if "hindi" in text:
        return "Hindi"
    if "telugu" in text:
        return "Telugu"
    if "english" in text:
        return "English"
    return None


# -------------------------------
# Transcript fetch
# -------------------------------
def fetch_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        full_text = " ".join([line.text for line in transcript])
        return full_text
    except Exception as e:
        print("Transcript error:", e)
        return None


# -------------------------------
# Main bot handler
# -------------------------------
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id
    user_message = update.message.text.strip()

    # -------- LANGUAGE CHANGE --------
    lang = detect_language(user_message)
    if lang:
        user_language[user_id] = lang
        await update.message.reply_text(f"Okay! I will reply in {lang} 🙂")
        return

    language = user_language.get(user_id, "English")

    # -------- TRANSLATE SUMMARY --------
    if ("summary" in user_message.lower() or "translate" in user_message.lower()) and user_id in user_last_summary:

        translate_prompt = f"""
Translate the following summary into {language}.
Do NOT add new information.
Do NOT answer anything else.

Summary:
{user_last_summary[user_id]}
"""

        translated = ask_openclaw(translate_prompt)
        await update.message.reply_text(translated)
        return

    # -------- CHECK YOUTUBE LINK --------
    video_id = extract_video_id(user_message)

    if video_id:
        await update.message.reply_text("Reading video and generating summary ⏳")

        full_text = fetch_transcript(video_id)

        if not full_text:
            await update.message.reply_text("This video does not have captions/subtitles available.")
            return

        user_video_context[user_id] = full_text

        text_chunk = full_text[:3500]

        prompt = f"""
You are an AI video assistant.

Summarize the YouTube video in {language}.

Provide:
• 5 key bullet points
• One clear final takeaway

Transcript:
{text_chunk}
"""

        summary = ask_openclaw(prompt)

        # store summary
        user_last_summary[user_id] = summary

        await update.message.reply_text(summary)
        return

    # -------- QUESTION ANSWERING --------
    if user_id not in user_video_context:
        await update.message.reply_text("Please send a YouTube video link first.")
        return

    await update.message.reply_text("Thinking... 🤔")

    transcript = user_video_context[user_id][:4000]

    prompt = f"""
You are a STRICT video assistant.

Rules you MUST follow:
1) Only answer using the transcript.
2) If the answer is not present, reply EXACTLY:
This topic is not covered in the video.
3) Do NOT use outside knowledge.
4) Do NOT guess.

Transcript:
{transcript}

Question:
{user_message}

Answer:
"""

    answer = ask_openclaw(prompt)
    await update.message.reply_text(answer)


# -------------------------------
# Run bot
# -------------------------------
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))

print("Telegram bot running...")
app.run_polling()