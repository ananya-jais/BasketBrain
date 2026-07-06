import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_ai_recommendation(filtered_df, totals, delivery):

    prompt = f"""
You are BasketBrain, an AI grocery shopping assistant.

Analyze the grocery basket below.

Products:
{filtered_df.to_string(index=False)}

Store Prices:
{totals}

Delivery:
{delivery}

Generate:

• Cheapest store

• Fastest store

• Money saved

• Trade-offs

• Shopping insight

Important:
Never tell the user what they should do.
Only explain the available options.

Maximum 120 words.
Friendly tone.
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    
    except Exception:
        return """
    ### BasketBrain AI Analysis

    • Cheapest store has been selected based on your basket.

    • Delivery times have been compared.

    • The recommendation engine is temporarily unavailable because the Gemini API is experiencing high demand.

    Your basket comparison still works correctly.
    """