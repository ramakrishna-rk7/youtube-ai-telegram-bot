import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

def ask_openclaw(prompt):

    payload = {
        "model": "kimi-k2.5:cloud",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=300)

        if r.status_code != 200:
            return f"Model error {r.status_code}: {r.text}"

        data = r.json()
        return data["message"]["content"]

    except Exception as e:
        return f"Model connection error: {e}"