import os

API_ID    = os.environ.get("API_ID"24349144 "")
API_HASH  = os.environ.get("API_HASH"c2620447969162e43504e9ad1b41f566"")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
