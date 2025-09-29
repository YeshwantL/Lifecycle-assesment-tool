import google.generativeai as genai
import os
import dotenv as load_dotenv

load_dotenv()
genai_key="AIzaSyD5m_OWlLrFlZGIjaWumCDfUvfjnCRCh8Q"

genai.configure(genai_key)

def predict_energy_if_missing():
    try:
        model=genai.GenerativeModel('gemini-pro')
        response=model.generate_content(detailed_prompt)
        return response.text
    except Exception as e:
        print(f"Error has occured {e}")
        return None
    
if __name__=='__main__':
    detailed_prompt=