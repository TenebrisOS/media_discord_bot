import discord
import io
import pyaudio
import time
import numpy as np
from matplotlib import pyplot as plt
import json

with open('C:/Users/modib/Documents/kali/py/MusicBot/config.json') as f:
   data = json.load(f)

# region variables 
TOKEN = data["TOKEN"]
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
ctx = "*"
#endregion

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="my Master orders :)"))

async def Play(message):
    channel = ctx.author.voice.channel
    if channel == None :
        await message.channel.Send("You aren't in a voice channel yet!")
    else :
        vc = await channel.connect()
        await message.channel.send("Joined Successfully!")

async def Stop(message):
    channel = ctx.author.voice.channel
    await message.voice_client.disconnect()

@client.event
async def on_message(message:discord.Message):
    if message.author.bot or not(str(message.content).startswith(ctx)):
        return
    if message.channel.id == (ctx, "Start") :
        Play
    if message.channel.id == (ctx, "Stop") :
        Stop

client.run(TOKEN)