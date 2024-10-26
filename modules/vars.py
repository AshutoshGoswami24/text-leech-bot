import os

API_ID    = os.environ.get("API_ID", "22690616")
API_HASH  = os.environ.get("API_HASH", "a4c943ff297671e2cfe8c3030a3fa7ae")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7103740355:AAGGjdNE610245GgTTO1nNkhxckjjcp-Pj0") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
