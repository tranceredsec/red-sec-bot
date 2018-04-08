import discord
from discord.ext import commands
from discord.ext.commands import bot
import time
import asyncio
import logging

client = discord.Client()

logging.basicConfig(level=logging.INFO)

@client.event
async def on_ready():
    print('[+] Username: ' + str(client.user.name))

@client.event
async def on_message(message):
    if message.content.startswith("$hfihgasdghfguaf"):
        await client.send_message(message.channel, "hello")
    elif message.content.startswith("$whoisskelly"):
        await client.send_message(message.channel, "https://i.pinimg.com/originals/e1/46/d0/e146d0ef3cad5e6ede22901c2107412d.jpg")
    elif message.content.startswith("$ping"):
        await client.send_message(message.channel, "Pong! :ping_pong:")
    elif message.content.startswith("$myid"):
        UserID = message.author.id
        await client.send_message(message.channel, "your user ID is: <@{}>".format(UserID) )
    elif message.content.startswith("$help"):
        await client.send_message(message.channel, "My owner is lazy and hasnt put a help menu in yet, just ask him what commands I can do")
    
                
client.run('NDEwMjQxNTQ5NjE2Njc2ODc1.DVrDYQ.ysPEDq-A32Ai-GtoeZ_bIvkjAVM')