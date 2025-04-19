import os

API_ID    = os.environ.get("API_ID", "29773843")
API_HASH  = os.environ.get("API_HASH", "8b40e91c29a00fecb905d6eb6aee2b3b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7673624928:AAE-kr8fIglNA8qy91KM99P-7hbTHUrRoKA") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
