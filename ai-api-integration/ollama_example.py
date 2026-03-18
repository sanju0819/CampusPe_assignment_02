import requests

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data["response"]

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")

    result = query_ollama(user_prompt)

    print("\nAI Response:\n")
    print(result)