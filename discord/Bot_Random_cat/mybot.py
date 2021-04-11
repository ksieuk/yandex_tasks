import discord
from discord.ext import commands


def get_prefix(client, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""
    prefixes = ['yandex!']

    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(client, message)


initial_extensions = ['cogs.random_cat']

bot = commands.Bot(command_prefix=get_prefix, description='Yandex...')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')


TOKEN = "NjkwMTAyOTQzNTM3ODIzNzU1.XnMicw.SM3Z1pief1dVUd8y1Vic-Dx4elU"
bot.run(TOKEN, bot=True, reconnect=True)
