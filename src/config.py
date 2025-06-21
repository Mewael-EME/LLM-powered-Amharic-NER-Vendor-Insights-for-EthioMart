from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"
CHANNELS = [
    "@ZemenExpress", "@nevacomputer", "@meneshayeofficial",
    "@ethio_brand_collection", "@Leyueqa"
]

RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"
IMAGES_PATH = "images/"
