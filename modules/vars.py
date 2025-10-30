import os

API_ID    = os.environ.get("API_ID", "20788544")
API_HASH  = os.environ.get("API_HASH", "2fe2e761f2222dbde043ab1639051761")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
