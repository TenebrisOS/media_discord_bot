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
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from discord.ext.commands import Bot
from discord.ext import commands

with open('C:/Users/modib/Documents/kali/py/MusicBot/config.json') as f:
   data = json.load(f)

# region variables 
TOKEN = data["TOKEN"]
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
PREFIX = "*"
SP_CLIENT_SECRET = data["SP_CLIENT_SECRET"]
SP_CLIENT_ID = data["SP_CLIENT_ID"]
tree = app_commands.CommandTree(client)
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SP_CLIENT_ID, client_secret=SP_CLIENT_SECRET))
#endregion

async def leavevoice(ctx):
    channel = ctx.author.voice.channel
    vc_d = channel.disconnect()
    await vc_d
    print("Left Voice Channel")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="my Master orders :)"))

@client.event
async def on_message(message:discord.Message):
    if message.author.bot or not(str(message.content).startswith(PREFIX)):
        return
    args = message.content.split(" ")
    args[0] = args[0][1::]
    print(args[0])
    if args[0] == "Start":
        await message.channel.send("Comingg !!!")
        channel = message.author.voice.channel
        vc_c = channel.connect()
        await vc_c
        print("Joined Voice Channel", channel)
        await message.channel.send("Joined Successfully!")
        if channel is None :
            await message.channel.send("You aren't in a voice channel yet!")
    elif args[0] == "Stop":
        async def leavevoice(ctx):
            channel = ctx.author.voice.channel
            vc_d = channel.disconnect()
            await vc_d
            print("Left Voice Channel")

client.run(TOKEN)