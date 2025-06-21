import os
import json
import re
from tqdm import tqdm
from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def normalize_amharic(text):
    if not text:
        return ""
    # Example normalization: remove extra spaces, unify digits, etc.
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)  # multiple spaces → one
    # Add Amharic-specific normalization here if needed
    return text

def preprocess_messages():
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    files = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith(".json")]

    for file in tqdm(files):
        raw_path = os.path.join(RAW_DATA_PATH, file)
        with open(raw_path, "r", encoding="utf-8") as f:
            messages = json.load(f)

        processed = []
        for msg in messages:
            clean_msg = normalize_amharic(msg.get("message", ""))
            if clean_msg:
                processed.append({
                    "channel": msg["channel"],
                    "message": clean_msg,
                    "views": msg.get("views"),
                    "date": msg.get("date"),
                    "media": msg.get("media")
                })

        processed_path = os.path.join(PROCESSED_DATA_PATH, file)
        with open(processed_path, "w", encoding="utf-8") as f:
            json.dump(processed, f, ensure_ascii=False, indent=2)
    print("All messages preprocessed and saved.")
