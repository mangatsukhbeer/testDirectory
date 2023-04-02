from discord import SyncWebhook
import discord
import dotenv
import os

dotenv.load_dotenv()
discord_hook = os.environ.get("hook")
webhook = SyncWebhook.from_url(discord_hook)
with open("/home/runner/work/testDirectory/testDirectory/log.txt") as file:
    data = discord.File(file)

webhook.send(file=data)
