import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_ai_recommendation(filtered_df, totals, delivery):

    prompt = f"""
You are BasketBrain.

Products:
{filtered_df.to_string(index=False)}

Prices:
{totals}

Delivery:
{delivery}

Recommend the best store.
Keep it under 120 words.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text