# ollama_client.py
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

LABELS = ["Education", "Skills", "Experience", "Projects", "Other"]

def call_ollama(prompt: str, model_name: str) -> str:
    """
    Call the local Ollama model with a given prompt and model_name.
    Returns the raw text response.
    """
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0  # deterministic
            }
        },
        timeout=120
    )
    response.raise_for_status()
    data = response.json()
    return data["response"].strip()

def slm_classify(text: str, model_name: str) -> str:
    """
    Ask the model to classify the resume line into one of the fixed labels.
    Returns one of LABELS (best effort).
    """
    prompt = f"""
You are a classifier for resume content.

You must classify the following line of text into EXACTLY ONE of these categories:
- Education
- Skills
- Experience
- Projects
- Other

Return ONLY the category name, nothing else.

Text:
\"\"\"{text}\"\"\""""

    raw = call_ollama(prompt, model_name=model_name)

    cleaned = raw.strip().lower()
    for label in LABELS:
        if label.lower() in cleaned:
            return label

    # Fallback if model returns something unexpected
    return "Other"