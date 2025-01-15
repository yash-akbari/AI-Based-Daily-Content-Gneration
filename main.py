import time
import logging
from config import Config
from services import GeminiService
from prompt_builder import PromptBuilder
from file_manager import FileManager

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def main():
    print("--- 🚀 Starting Blog Generator ---")

    # 1. Validate Environment
    try:
        Config.validate()
    except ValueError as e:
        logger.critical(e)
        return

    # 2. Load Data
    try:
        df = FileManager.load_topics(Config.INPUT_FILE)
        logger.info(f"Loaded {len(df)} topics.")
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        return

    # 3. Initialize Service
    ai_service = GeminiService()

    # 4. Process Queue
    success_count = 0

    for index, row in df.iterrows():
        topic = row.get('Topic', 'Unknown')
        logger.info(f"Processing [{index + 1}/{len(df)}]: {topic}")

        try:
            # Build Prompt
            prompt = PromptBuilder.build_blog_prompt(row)

            # Generate Content
            content = ai_service.generate_text(prompt)

            # Save Content
            FileManager.save_markdown(content, topic)

            success_count += 1

        except Exception as e:
            logger.error(f"Failed to generate blog for '{topic}': {e}")

        # Rate Limiting
        time.sleep(Config.SLEEP_BETWEEN_CALLS)

    print(f"\n--- ✨ Job Complete. Generated {success_count}/{len(df)} blogs. ---")


if __name__ == "__main__":
    main()