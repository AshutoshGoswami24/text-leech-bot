import os

API_ID    = os.environ.get("22946135", "")
API_HASH  = os.environ.get("93e1b0c387cabe34a3ccfa1724ae8527", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
