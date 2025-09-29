import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# It's recommended to load the API key from an environment variable for security.
# Create a .env file in this directory with the following content:
# GENAI_API_KEY="your_google_api_key"
genai_key = os.getenv("AIzaSyD5m_OWlLrFlZGIjaWumCDfUvfjnCRCh8Q")

if not genai_key:
    raise ValueError("GENAI_API_KEY not found. Please set it in your .env file.")

genai.configure(api_key=genai_key)

def predict_energy_if_missing(prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error has occurred: {e}")
        return None

# This block runs ONLY when you execute this script directly
if __name__ == '__main__':
    # Define the detailed prompt
    detailed_prompt = "Provide the average energy consumption in kWh/ton for primary aluminum smelting based on recent public data."

    # Call the function with the prompt
    estimated_value = predict_energy_if_missing(detailed_prompt)

    if estimated_value:
        print("Gemini's Response:")
        print(estimated_value)