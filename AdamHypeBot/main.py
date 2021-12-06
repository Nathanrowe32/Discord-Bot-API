#Discord bot that is a personal hype man.
#When the correct targetID (discord username) joins a voice channel, the bot will follow and play a sound.
#TOKEN from the last line is the bot's token key. Replace with your own bot's token to run on your server.
#import required dependencies
from discord.ext import commands

#import Bot Token
from functions import *

intents = discord.Intents.default()
intents.members = True

#! is the command prefix to run commands.
client = commands.Bot(command_prefix = '%', intents=intents)

#Will print when the bot is online.
@client.event
async def on_ready():
    print("{0.user} IS ONLINE." .format(client))


#%HypeBot prints a hype line.
@client.command()
async def HypeBot(ctx):
    author = str(ctx.message.author).split("#")[0]
    await ctx.send("`Yo yo yo " + author + ", i'm " + targetID + "'s hype bot! :D`")


#%join will make the bot join the voice channel you are on.
@client.command()
async def join(ctx):
    channel = ctx.author.voice
    if str(channel) == 'None':
        await ctx.channel.send('`You have to be in a voice channel to use this command.`')
    else :
        channel = ctx.author.voice.channel
        await channel.connect()


#%leave will make the bot leave the voice channel.
@client.command(pass_context = True)
async def leave(ctx):
    await ctx.voice_client.disconnect()

#% will make the bot join the voice channel the sender is in and play audio file.
@client.command()
async def raid(ctx):
    channel = ctx.author.voice
    if str(channel) == 'None':
        await ctx.channel.send('`You have to be in a voice channel to use this command.`')
    else:
        await attackTarget(ctx.author, client)

#When the targetID joins a voice channel, the bot will follow and play the audio_source file.
#Does a quick check to see if the member that joined is the targetID, if yes then go in and play, else print "not target".
@client.event
async def on_voice_state_update(member, before, after):
    # user joins a server
    if before.channel is None and after.channel is not None:
        if str(member) == targetID:
            print(targetID + " has joined the channel, and is under attack :)")
            await attackTarget(member, client)
        else:
            print(str(member) + " has joined " + str(after.channel) + ", and is not the target.")
    # user leaves the server
    elif before.channel is not None and after.channel is None:
        if str(member) == targetID:
            print("targetID has left " + str(before.channel))
            await disconnectBot(client)
        else:
            print(str(member) + " has left " + str(before.channel) + ", and is not the target.")
    # user relocates from one channel to another.
    else:
        if str(member) == targetID:
            print(targetID + " has relocated from " + str(before.channel) + " to " + str(after.channel))
            await targetRelocated(member, before, after, client)

#Replace TOKEN with your bot's token to run.
client.run(TOKEN);
