def query_ollama(model, prompt, temperature=0):
    import os
    import openai
    import requests

    # Correct setup for Ollama-compatible local OpenAI client
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}

    payload = {
        "model":model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "stream": False
    }
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["message"]["content"]

    # Safely access the message content
    #return response.choices[0].message.content