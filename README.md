# 🦞 OpenClaw AI Agent — YouTube Video Summarizer & Q&A Telegram Bot

An **OpenClaw-style AI agent application** that reads a YouTube video, understands its content, summarizes it, and answers questions grounded strictly in the video transcript.

This project demonstrates how an LLM agent can use external tools (YouTube transcript retrieval) to produce reliable answers instead of hallucinating.

---

## 🎯 Project Goal

Build an AI assistant where:

* A user interacts through Telegram
* The AI agent retrieves real information from a tool
* The model reasons over that information
* The assistant answers only from verified context

This follows the **OpenClaw agent philosophy**:

> LLM + Tools + Grounding = Reliable AI assistant

---

## ✨ Features

* Accepts YouTube video links
* Extracts subtitles automatically
* Generates structured summary
* Answers follow-up questions
* Multi-language responses (English / Hindi / Telugu)
* Context memory per user
* Hallucination prevention (grounded answering)
* Fully local AI inference

---

## 🧠 OpenClaw Agent Architecture

```id="c9e0yq"
Telegram User
      ↓
Agent Interface (Telegram Bot)
      ↓
OpenClaw-style Tool Invocation
      ↓
YouTube Transcript Tool (Python)
      ↓
Context Injection (RAG Prompt)
      ↓
Local LLM (Ollama - Kimi)
      ↓
Grounded Response
```

Instead of answering from training data, the agent **retrieves information first and reasons over it**.

---

## 🔍 Why OpenClaw Matters

Traditional chatbots:

> Ask model → model guesses → hallucination risk

OpenClaw-style agent:

> Ask model → model calls tool → receives data → model reasons → reliable answer

This project demonstrates **tool-augmented reasoning**, a core concept of modern AI agents.

---

## 🛠️ Technology Stack

| Layer                   | Technology                    |
| ----------------------- | ----------------------------- |
| Agent Interaction       | Telegram Bot API              |
| Agent Framework Concept | OpenClaw-style tool reasoning |
| Tool                    | YouTube Transcript API        |
| LLM Runtime             | Ollama                        |
| Model                   | kimi-k2.5                     |
| Language                | Python                        |

---

## 📦 Installation

### 1. Clone Repository

```id="60wq0a"
git clone https://github.com/YOUR_USERNAME/youtube-ai-telegram-bot.git
cd youtube-ai-telegram-bot
```

---

### 2. Create Virtual Environment

```id="o9fns7"
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```id="u2a24j"
pip install -r requirements.txt
```

---

## 🤖 Install Ollama (Required)

Download:
https://ollama.com/download

Start server:

```id="4hgn1p"
ollama serve
```

Download model:

```id="66pfq4"
ollama pull kimi-k2.5:cloud
```

---

## 🦞 Install OpenClaw (Agent Framework Demonstration)

Install Node.js (v20+):
https://nodejs.org

Verify:

```id="h9jv4p"
node -v
npm -v
```

Install OpenClaw:

```id="t67u7y"
npm install -g openclaw
```

Start gateway:

```id="6yq2v9"
openclaw gateway
```

Open UI:

```id="f8ayjz"
http://127.0.0.1:18791
```

(OpenClaw is used to demonstrate agent-tool orchestration concepts.)

---

## 🤖 Telegram Bot Setup

1. Open Telegram
2. Search **@BotFather**
3. Run:

```id="r3s4j7"
/newbot
```

Create `.env`:

```id="acjyo8"
TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

---

## ▶️ Run

Ensure Ollama is running.

```id="r4kntc"
python telegram_bot.py
```

Message the bot on Telegram.

---

## 💬 Example Interaction

Send:

```id="3c6g1s"
https://www.youtube.com/watch?v=8hly31xKli0
```

Ask:

```id="gyahj5"
What is the video about?
```

Change language:

```id="a5zsk3"
Hindi
Give summary
```

---

## 🛡️ Grounded AI (Anti-Hallucination)

If the question is unrelated:

```id="kw4qks"
Who won IPL 2023?
```

Bot replies:

```id="x6fa1h"
This topic is not covered in the video.
```

This proves the agent relies on retrieved data rather than memorized knowledge.

---

## 📁 Project Structure

```id="j9k20u"
telegram_bot.py
openclaw_client.py
requirements.txt
README.md
.env (excluded)
```

---

## 📚 Concepts Demonstrated

* AI Agents
* Tool Calling
* Retrieval Augmented Generation (RAG)
* Prompt Grounding
* Conversational Memory
* LLM Safety (hallucination prevention)

---

## 👨‍💻 Author

Rama Krishna
B.Tech Student – AI/Software Engineering Enthusiast

---

