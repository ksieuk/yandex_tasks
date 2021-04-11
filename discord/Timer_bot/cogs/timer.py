import discord
from discord.ext import commands
import asyncio


class Ailurophile(commands.Cog, name="Ailurophile"):
    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Готов быть таймером")

    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
            text = message.content
            if text.startswith("set_timer in"):
                hours, minutes = float(text.split()[-4]), float(text.split()[-2])
                seconds = 60 ** 2 * hours + 60 * minutes
                await message.channel.send(f"The time should start in {hours} hours {minutes} minutes")
                await asyncio.sleep(seconds)
                await message.channel.send("Time X has come!")


def setup(bot):
    bot.add_cog(Ailurophile(bot))
