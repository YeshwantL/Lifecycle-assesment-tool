import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Get API key from .env file
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Warning: GEMINI_API_KEY not found in .env file. Using a hardcoded key for now.")
    api_key = "AIzaSyD5m_OWlLrFlZGIjaWumCDfUvfjnCRCh8Q"  # Replace with your key

genai.configure(api_key=api_key)

def predict_energy_if_missing(prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error has occurred: {e}")
        return None

if __name__ == '__main__':
    detailed_prompt = "Provide the average energy consumption in kWh/ton for primary aluminum smelting based on recent public data."
    estimated_value = predict_energy_if_missing(detailed_prompt)
    if estimated_value:
        print("Gemini's Response:")
        print(estimated_value)
