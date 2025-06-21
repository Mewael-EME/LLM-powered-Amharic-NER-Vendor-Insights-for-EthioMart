from src.telegram_client import TelegramScraper
from src.data_cleaning import preprocess_messages
from src.config import CHANNELS, RAW_DATA_PATH, PROCESSED_DATA_PATH

def run_pipeline():
    scraper = TelegramScraper()
    for channel in CHANNELS:
        print(f"Fetching messages from {channel}...")
        scraper.fetch_and_save(channel)

    print("Preprocessing messages...")
    preprocess_messages()

if __name__ == "__main__":
    run_pipeline()
