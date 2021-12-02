#Discord bot that is a personal hype man.
#When the correct targetID (discord username) joins a voice channel, the bot will follow and play a sound.
#TOKEN from the last line is the bot's token key. Replace with your own bot's token to run on your server.
#import required dependencies
import asyncio
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random

#import Bot Token
from apikeys import *

intents = discord.Intents.default()
intents.members = True

#! is the command prefix to run commands.
client = commands.Bot(command_prefix = '!', intents=intents)
#targetID is the discord username that you want the bot to hype up.
targetID = "Space Adam#7320"

#Will print when the bot is online.
@client.event
async def on_ready():
    print("{0.user} IS ONLINE." .format(client))


#!AdamHypeBot prints a hype line.
@client.command()
async def AdamHypeBot(ctx):
    author = str(ctx.message.author).split("#")[0]
    await ctx.send("`Yo yo yo " + author + ", i'm adam's hype bot! :D`")


#!join will make the bot join the voice channel you are on.
@client.command()
async def join(ctx):
    channel = ctx.author.voice
    if str(channel) == 'None':
        await ctx.channel.send('`You have to be in a voice channel to use this command.`')
    else :
        channel = ctx.author.voice.channel
        await channel.connect()


#!leave will make the bot leave the voice channel.
@client.command(pass_context = True)
async def leave(ctx):
    await ctx.voice_client.disconnect()

#When the targetID joins a voice channel, the bot will follow and play the audio_source file.
#Does a quick check to see if the member that joined is the targetID, if yes then go in and play, else print "not target".
@client.event
async def on_voice_state_update(member, before, after):
    #audio_source is the file that will be played.
    audio_source = FFmpegPCMAudio("AdamHypeTrackFinal.mp3")
    if before.channel is None and after.channel is not None:
        if str(member) == targetID:
            channel = member.voice.channel
            await channel.connect()
            voice = discord.utils.get(client.voice_clients)
            voice.play(audio_source)
            await asyncio.sleep(10)
            await voice.disconnect()
        else:
            print("This is not the target")


#Replace TOKEN with your bot's token to run.
client.run(TOKEN);