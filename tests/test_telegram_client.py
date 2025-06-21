import pytest
from src.telegram_client import TelegramScraper

def test_fetch_and_save():
    scraper = TelegramScraper()
    # just test it doesn't raise exceptions for a known channel
    scraper.fetch_and_save("kuruwear", limit=2)
