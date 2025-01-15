import os
import pandas as pd
import re
import time
from pathlib import Path
from config import Config
import logging

logger = logging.getLogger(__name__)


class FileManager:
    @staticmethod
    def ensure_directory_exists(directory: Path):
        if not directory.exists():
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")

    @staticmethod
    def load_topics(filepath: Path) -> pd.DataFrame:
        if not filepath.exists():
            raise FileNotFoundError(f"Input file not found: {filepath}")
        return pd.read_csv(filepath)

    @staticmethod
    def save_markdown(content: str, topic: str):
        """Saves content to a sanitized filename."""
        FileManager.ensure_directory_exists(Config.OUTPUT_DIR)

        # Sanitize filename
        safe_title = re.sub(r'[^\w\s-]', '', topic).strip().lower()
        safe_title = re.sub(r'[-\s]+', '_', safe_title)

        filename = f"{safe_title}_{int(time.time())}.md"
        filepath = Config.OUTPUT_DIR / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        logger.info(f"Saved file: {filepath}")