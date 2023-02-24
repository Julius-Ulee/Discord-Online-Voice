import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

GUILD_ID = 706339390053416981
CHANNEL_ID = 1052064292750499931


@client.event
async def on_ready():
    print(f'Logged in as {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=True, self_deaf=False)
    print(f"Successfully joined {vc.name} ({vc.id})")

keep_alive()
client.run(os.getenv("TOKEN"))
