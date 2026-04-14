from discord import SyncWebhook
import os
from dotenv import load_dotenv
import db

load_dotenv()
discord_hook = os.getenv("discord_hook")

def send_discord():
    webook = SyncWebhook.from_url(discord_hook)
    query = db.collect()
    webook.send(query)