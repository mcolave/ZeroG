import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure GenAI
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def estimate_macros(food_description):
    """
    Uses Gemini to estimate the macronutrients of a described food.
    Returns a dictionary of macros or None if it fails.
    """
    if not api_key:
        print("DEBUG: Gemini API Key not found, skipping AI estimation.")
        return None
        
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        prompt = f"""
        You are a highly accurate nutrition database API. I will provide you with a food or meal description.
        You must estimate its nutritional values.
        
        Note: The food description might be in English, Filipino (Tagalog), or Taglish. Please translate and adapt to local Filipino foods, dishes, and measurement units if necessary.
        
        Food: "{food_description}"
        
        Respond ONLY with a raw JSON object and nothing else (no markdown formatting, no explanations). The JSON object must have exactly these keys:
        {{
            "carbs": <float, grams>,
            "fats": <float, grams>,
            "protein": <float, grams>,
            "calories": <float, kcal>,
            "potassium": <float, mg>,
            "sodium": <float, mg>,
            "saturated_fat": <float, grams>,
            "trans_fat": <float, grams>,
            "gi": <int, estimated glycemic index 0-100>
        }}
        If a value is unknown, make your best reasonable estimate.
        """
        
        print(f"DEBUG: Asking Gemini for macros of '{food_description}'...")
        
        # Retry logic for 429 Quota Exhausted
        import time
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = model.generate_content(prompt)
                break # Success
            except Exception as e:
                err_str = str(e)
                if '429' in err_str and attempt < max_retries - 1:
                    print(f"DEBUG: Hit rate limit (429). Retrying in 65 seconds... (Attempt {attempt+1})")
                    time.sleep(65)
                else:
                    raise e
                    
        text = response.text.strip()
        
        # Clean potential markdown formatting
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
            
        data = json.loads(text.strip())
        
        # Ensure all required keys are present
        required_keys = ['carbs', 'fats', 'protein', 'calories', 'potassium', 'sodium', 'saturated_fat', 'trans_fat', 'gi']
        for key in required_keys:
            if key not in data:
                data[key] = 0.0
                
        # Set name and source
        data['name'] = food_description.lower().strip()
        data['source'] = 'gemini_ai'
        
        print(f"DEBUG: Gemini successfully estimated macros for '{food_description}'")
        return data
        
    except Exception as e:
        print(f"DEBUG: Gemini AI estimation failed: {e}")
        return None
