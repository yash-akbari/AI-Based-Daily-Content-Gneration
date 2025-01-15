import google.generativeai as genai
from config import Config
import logging

# Configure Logging
logger = logging.getLogger(__name__)

class GeminiService:
    def __init__(self):
        genai.configure(api_key=Config.API_KEY)
        self.model = genai.GenerativeModel(Config.MODEL_NAME)

    def generate_text(self, prompt: str) -> str:
        """
        Sends a prompt to Gemini and returns the text response.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"API Error: {e}")
            raise e