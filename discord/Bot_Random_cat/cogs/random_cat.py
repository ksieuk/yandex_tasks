import discord
from discord.ext import commands
import requests


class Ailurophile(commands.Cog, name="Ailurophile"):
    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Готов показать случайного котика (или пёсика!)")

    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
            text = message.content
            if "кот" in text or "кошк" in text:
                file = requests.get(f"https://api.thecatapi.com/v1/images/search").json()[0]["url"]
                await message.channel.send(file)
            elif "собак" in text or "собачк" in text:
                file = requests.get(f"https://dog.ceo/api/breeds/image/random").json()["message"]
                await message.channel.send(file)


def setup(bot):
    bot.add_cog(Ailurophile(bot))
