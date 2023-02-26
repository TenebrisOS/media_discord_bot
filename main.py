import discord
import io
import pyaudio
import time
import numpy as np
from matplotlib import pyplot as plt
import json
from discord.ext import commands
from dislash import InteractionClient
from discord import app_commands
from discord import __author__
import asyncio
from discord.ext import commands

with open('C:/Users/modib/Documents/kali/py/MusicBot/config.json') as f:
   data = json.load(f)

# region variables 
TOKEN = data["TOKEN"]
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
PREFIX = "*"
tree = app_commands.CommandTree(client)
#endregion

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="my Master orders :)"))

@client.event
async def Leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    print("Left Voice Channel")

@client.event
async def on_message(message:discord.Message):
    if message.author.bot or not(str(message.content).startswith(PREFIX)):
        return
    args = message.content.split(" ")
    args[0] = args[0][1::]

    if args[0] == "Start":
        await message.channel.send("Comingg !!!")
    channel = message.author.voice.channel
    vc = channel.connect()
    print("Joined Voice Channel")
    await message.channel.send("Joined Successfully!")
    if channel is None :
        await message.channel.send("You aren't in a voice channel yet!")

    elif args[0] == "Stop" :
        server = message.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    print("Left Voice Channel")

client.run(TOKEN)