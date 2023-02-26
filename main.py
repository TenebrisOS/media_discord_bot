import discord
import io
import pyaudio
import time
import json
from discord import app_commands
import asyncio
import pytube as pt
from pytube import YouTube
import os
import ffmpeg

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

    if args[0] == "Stop":
        async def leavevoice(ctx):
            channel = ctx.author.voice.channel
            vc_d = channel.disconnect()
            await vc_d
            print("Left Voice Channel")
    
    if args[0] == "Help":
        mbd = discord.Embed(title='Help')
        mbd.color = discord.Color.orange()
        mbd.add_field(name="Usage", value="*Play <youtube link>")
        await message.channel.send(embed=mbd)

    if args[0] == "Play":
        await message.channel.send("Ok.")
        print("Downloading", args[1])
        yt = YouTube(args[1])
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path="C:/Users/modib/Videos/Captures/")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        await message.channel.send("Succefully added to Playlist")
        channel = message.author.voice.channel
        if channel is None :
            await message.channel.send("You are not in a voice channel yet!")
        print("Joined Voice Channel", channel)
        await message.channel.send("Joined Successfully!")
        voice = await message.author.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio(new_file, executable="C:/ffmpeg/bin/ffmpeg.exe"))

    else :
        await message.channel.send("Unknown Command")

client.run(TOKEN)