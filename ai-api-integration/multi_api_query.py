import os
from dotenv import load_dotenv
from groq import Groq
from openai import OpenAI
import cohere

load_dotenv()

# Initialize clients
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

hf_client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HUGGINGFACE_API_KEY"),
)

cohere_client = cohere.ClientV2(os.getenv("COHERE_API_KEY"))


def query_groq(prompt):
    try:
        response = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


def query_huggingface(prompt):
    try:
        completion = hf_client.chat.completions.create(
            model="moonshotai/Kimi-K2-Instruct-0905",
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


def query_cohere(prompt):
    try:
        response = cohere_client.chat(
            model="command-a-03-2025",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {e}"


def main():
    print("Choose AI Provider:")
    print("1. Groq")
    print("2. HuggingFace")
    print("3. Cohere")

    choice = input("Enter choice (1-3): ")
    prompt = input("Enter your prompt: ")

    if choice == "1":
        result = query_groq(prompt)
    elif choice == "2":
        result = query_huggingface(prompt)
    elif choice == "3":
        result = query_cohere(prompt)
    else:
        result = "Invalid choice"

    print("\nAI Response:\n")
    print(result)


if __name__ == "__main__":
    main()