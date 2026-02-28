from openclaw.llms.ollama import Ollama

# connect OpenClaw to your local model
llm = Ollama(model="phi3:mini")

def ask_ai(prompt):
    response = llm.invoke(prompt)
    return response