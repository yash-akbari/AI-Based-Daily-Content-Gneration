import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = 'gemini-1.5-flash'

    # Paths
    BASE_DIR = Path(__file__).parent
    INPUT_FILE = BASE_DIR / "topics.csv"
    OUTPUT_DIR = BASE_DIR / "generated_blogs"

    # Rate Limiting
    SLEEP_BETWEEN_CALLS = 2  # seconds

    @staticmethod
    def validate():
        if not Config.API_KEY:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")