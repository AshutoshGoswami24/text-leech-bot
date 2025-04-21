import os

API_ID    = os.environ.get("API_ID", "20607064")
API_HASH  = os.environ.get("API_HASH", "c0a09fd762681a66366cf84976f31a17")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
