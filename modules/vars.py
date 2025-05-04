import os

API_ID    = os.environ.get("API_ID", "21502917")
API_HASH  = os.environ.get("API_HASH", "fbd85bad63b38d8c0f2c0fd6202f413b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
