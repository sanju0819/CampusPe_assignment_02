import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize HuggingFace client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)

def query_huggingface(prompt):
    try:
        completion = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Instruct-0905",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")

    result = query_huggingface(user_prompt)

    print("\nAI Response:\n")
    print(result)