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
                text = text.split()[2:]

                if not all((text[0].isdigit(), text[1] == "hours", text[2] == "and", text[3].isdigit(), text[4] == "minutes.")):
                    return

                hours, minutes = float(text[0]), float(text[3])
                if hours == int(hours):
                    hours = int(hours)
                if minutes == int(minutes):
                    minutes = int(minutes)

                seconds = 60 ** 2 * hours + 60 * minutes
                await message.channel.send(f"The time should start in {hours} hours {minutes} minutes")
                await asyncio.sleep(seconds)
                await message.channel.send("Time X has come!")


def setup(bot):
    bot.add_cog(Ailurophile(bot))
