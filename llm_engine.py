import requests

def ask_llm(question):

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "tinyllama",
        "prompt": f"Answer this interview question in 2 short sentences:\n{question}",
        "stream": False,
        "options": {
            "num_predict": 60
        }
    }

    r = requests.post(url, json=payload)

    return r.json()["response"]