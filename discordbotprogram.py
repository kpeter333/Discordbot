import discord
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']



class MyClient(discord.Client):
    async def on_ready(self):
        print("logged on as {0}!".format(self.user))

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))  # still useful for you
        channel = self.get_channel(1427207526557945858)  # replace with your channel ID
        await channel.send("Hey everyone! I'm KelvinBot! 👋")


    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("hello"):
            await message.channel.send("Hello World!")

        if message.content.startswith("meme"):
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))

