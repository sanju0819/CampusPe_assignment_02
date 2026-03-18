import os
import cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Cohere client
co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.message.content[0].text

    except Exception as e:
        return f"Error: {e}"


# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")

    print("Querying Cohere API...")

    result = query_cohere(user_prompt)

    print("\nAI Response:\n")
    print(result)