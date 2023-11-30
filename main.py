import os
import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.AzureOpenAI(
    api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
    api_version="2023-08-01-preview",
    azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
)


def get_response(message):
    completion = client.chat.completions.create(
        model=os.environ.get("DEPLOYMENT_NAME"),
        messages=[
            {
                "role": "user",
                "content": "How is Azure machine learning different than Azure OpenAI?",
            },
        ]
    )
    
    response = f"{completion.choices[0].message.role}: {completion.choices[0].message.content}"
    
    return response

print()