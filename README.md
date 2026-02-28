# 🎥 AI YouTube Video Summarizer & Q&A Telegram Bot

An intelligent Telegram assistant that reads a YouTube video, understands its content, summarizes it, and answers user questions **strictly based on the video transcript**.

This project demonstrates a practical **Retrieval-Augmented Generation (RAG)** system using a local LLM.

---

## 🚀 Features

* 🔗 Accepts any YouTube video link
* 🧠 Automatically extracts video transcript
* 📝 Generates structured summary (5 key points + takeaway)
* ❓ Answers follow-up questions from the video
* 🌐 Multi-language support (English / Hindi / Telugu)
* 🚫 Prevents hallucinations (will refuse unrelated questions)
* 💬 Fully interactive Telegram chat interface
* 🏠 Runs locally using an LLM (no OpenAI API required)

---

## 🧠 How It Works

User sends a YouTube link →
Bot extracts transcript →
Transcript is given to local LLM →
LLM summarizes and answers questions →
Bot replies inside Telegram.

This follows a **RAG architecture**:

```
Telegram User
      ↓
Python Telegram Bot
      ↓
YouTube Transcript API
      ↓
Prompt + Context Injection
      ↓
Local LLM (Ollama – Kimi model)
      ↓
Grounded Response
```

---

## 🛠️ Tech Stack

| Component            | Technology             |
| -------------------- | ---------------------- |
| Language             | Python 3.12            |
| Chat Interface       | Telegram Bot API       |
| LLM Runtime          | Ollama                 |
| Model                | kimi-k2.5              |
| Transcript Retrieval | youtube-transcript-api |
| Prompting            | Grounded RAG Prompting |
| HTTP Communication   | requests               |

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/youtube-ai-bot.git
cd youtube-ai-bot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Ollama

Download and install:
https://ollama.com

Start Ollama:

```bash
ollama serve
```

Pull model:

```bash
ollama pull kimi-k2.5:cloud
```

---

## 🤖 Create Telegram Bot

1. Open Telegram
2. Search **@BotFather**
3. Run:

```
/newbot
```

4. Copy the API Token
5. Paste it inside:

```
telegram_bot.py
TOKEN = "YOUR_TOKEN_HERE"
```

---

## ▶️ Run the Project

Start the bot:

```bash
python telegram_bot.py
```

Open Telegram and message your bot.

---

## 💡 Example Usage

Send:

```
https://www.youtube.com/watch?v=8hly31xKli0
```

Bot replies with structured summary.

Ask:

```
What is the video about?
```

Change language:

```
Hindi
Give summary
```

---

## 🛡️ Hallucination Protection

The assistant is intentionally restricted:

If a question is unrelated to the video, it replies:

```
This topic is not covered in the video.
```

Example:

```
Who won IPL 2023?
→ This topic is not covered in the video.
```

This demonstrates grounded AI behavior.

---

## 📁 Project Structure

```
youtube-ai-bot/
│
├── telegram_bot.py        # Main Telegram interface
├── openclaw_client.py     # LLM communication
├── get_transcript.py      # Transcript testing
├── summarize_video.py     # Prompt logic
├── requirements.txt
└── README.md
```

---

## 📌 Future Improvements

* Vector database memory (FAISS/Chroma)
* Timestamped answers
* Multiple video sessions
* Voice message support
* Web interface

---

## 👨‍💻 Author

Rama Krishna
B.Tech Student – AI/ML Software Engineering Enthusiast

---

## ⭐ What This Project Demonstrates

* Prompt Engineering
* RAG (Retrieval Augmented Generation)
* LLM grounding
* Conversational memory
* API integration
* Real-world AI application design

---

