from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

models = client.models.list()

for model in models:
    print("MODEL:", model.name)
    print("SUPPORTED METHODS:", model.supported_actions)
    print("-" * 50)