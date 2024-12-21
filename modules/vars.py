import os

API_ID    = os.environ.get("API_ID", "28590286")
API_HASH  = os.environ.get("API_HASH", "6a68cc6b41219dc57b7a52914032f92f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
