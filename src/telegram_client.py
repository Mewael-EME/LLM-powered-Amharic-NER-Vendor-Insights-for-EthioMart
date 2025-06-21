import os
import json
from telethon.sync import TelegramClient  # for scripts like main.py
from telethon import TelegramClient as AsyncTelegramClient  # for async use
from src.config import API_ID, API_HASH, RAW_DATA_PATH

class TelegramScraper:
    def __init__(self):
        # Synchronous client (used only in script, e.g., main.py)
        self.client = TelegramClient("ethio_client", API_ID, API_HASH)
        # Asynchronous client (for notebooks)
        self.async_client = AsyncTelegramClient("ethio_client", API_ID, API_HASH)

    def fetch_and_save(self, channel, limit=200):
        """For script-based synchronous use"""
        messages = []
        with self.client:
            for msg in self.client.iter_messages(channel, limit=limit):
                msg_dict = {
                    "channel": channel,
                    "message": msg.message,
                    "date": str(msg.date),
                    "views": msg.views,
                    "media": None
                }
                messages.append(msg_dict)

        os.makedirs(RAW_DATA_PATH, exist_ok=True)
        file_path = os.path.join(RAW_DATA_PATH, f"{channel.strip('@')}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        print(f"[SYNC] Saved {len(messages)} messages from {channel} to {file_path}")

    async def async_fetch_and_save(self, channel, limit=200):
        """For Jupyter Notebook async use"""
        messages = []
        async with self.async_client:
            async for msg in self.async_client.iter_messages(channel, limit=limit):
                msg_dict = {
                    "channel": channel,
                    "message": msg.message,
                    "date": str(msg.date),
                    "views": msg.views,
                    "media": None
                }
                messages.append(msg_dict)

        os.makedirs(RAW_DATA_PATH, exist_ok=True)
        file_path = os.path.join(RAW_DATA_PATH, f"{channel.strip('@')}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        print(f"[ASYNC] Saved {len(messages)} messages from {channel} to {file_path}")
