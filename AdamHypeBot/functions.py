import asyncio
import discord
from discord import FFmpegPCMAudio
from constants import *

#attacks the target with the hype audio.
async def attackTarget(member, client):
        # audio_source is the file that will be played.
        # creates a new audio source
        audio_source = FFmpegPCMAudio(audio_source_file)
        channel = member.voice.channel
        await channel.connect()
        voice = discord.utils.get(client.voice_clients)
        voice.play(audio_source)
        await asyncio.sleep(10)
        await disconnectBot(client)

#disconnects bot from voice channel.
async def disconnectBot(client):
    voice = discord.utils.get(client.voice_clients)
    #checks to see if the bot was in a channel, if not do nothing.
    if voice:
        await voice.disconnect()

#target relocated from one voice channel into another without disconnecting from server.
async def targetRelocated(member, before, after, client):
    if before.channel != after.channel:
        await disconnectBot(client)
        await attackTarget(member, client)
