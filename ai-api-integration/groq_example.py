import os
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_groq(prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant"
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")

    result = query_groq(user_prompt)

    print("\nAI Response:\n")
    print(result)