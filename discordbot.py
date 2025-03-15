import discord
import os
from datetime import datetime

bot_started_time = datetime.now().strftime("%m/%d/%y, %H:%M:%S") #Used here because it is only defined one it it run

def log(type, message, guild):
    time = datetime.now().strftime("%m/%d/%y, %H:%M:%S")
    print(f'[{type} LOG, {time}] {message} sent in {guild}')
    return

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return

token = input('Bot token: ')
cls()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    cls()
    log('SYSTEM', f'Logged in as {client.user}', "None")
    log('INFO', 'Bot is in the following guilds:', "None")
    for guild in client.guilds:
        print(f"- {guild.name} (ID: {guild.id})")
    print("")
    return
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "s!help":
        guild_name = message.guild.name if message.guild else "Direct Message"
        user_id = message.author.id
        username = message.author.name
        #
        if message.guild:
            guild_id = message.guild.id
        else:
            guild_id = f"{username}'s Direct Messages"
        #
        log('COMMAND', f"Command \"s!help\" sent by {username} [{user_id}]", guild_name)
        await message.channel.send("s!hi - Say hi to the bot, and it'll say hi back!\ns!info - Give info on the bot\ns!ping - Return the ping of the bot\ns!serverinfo - Return info on the current server")

    elif message.content == "s!hi":
        guild_name = message.guild.name if message.guild else "Direct Message"
        user_id = message.author.id
        username = message.author.name
        #
        if message.guild:
            guild_id = message.guild.id
        else:
            guild_id = f"{username}'s Direct Messages"
        #
        log('COMMAND', f"Command \"s!hi\" sent by {username} [{user_id}]", guild_name)
        await message.channel.send(f"Hello, <@{user_id}>!")

    elif message.content == "s!info":
        guild_name = message.guild.name if message.guild else "Direct Message"
        user_id = message.author.id
        username = message.author.name
        #
        if message.guild:
            guild_id = message.guild.id
        else:
            guild_id = f"{username}'s Direct Messages"
        #
        log('COMMAND', f"Command \"s!info\" sent by {username} [{user_id}]", guild_name)
        await message.channel.send(f"Bot started at {bot_started_time}.\nBot name: {client.user}")
    
    elif message.content == "s!ping":
        guild_name = message.guild.name if message.guild else "Direct Message"
        user_id = message.author.id
        username = message.author.name
        #
        if message.guild:
            guild_id = message.guild.id
        else:
            guild_id = f"{username}'s Direct Messages"
        #
        log('COMMAND', f"Command \"s!ping\" sent by {username} [{user_id}]", guild_name)
        latency = round(client.latency * 1000)
        await message.channel.send(f"Pong! Latency is {latency}ms.")

    elif message.content == "s!serverinfo":
        user_id = message.author.id
        username = message.author.name
        guild_name = message.guild.name if message.guild else "Direct Message"
        #
        if message.guild:
            guild_id = message.guild.id
        else:
            guild_id = f"{username}'s Direct Messages"
        #
        #
        if message.guild:
            guild_name = message.guild.name
            member_count = message.guild.member_count
        else:
            guild_name = "Direct Message"
            member_count = 0
        #
        log('COMMAND', f"Command \"s!serverinfo\" sent by {username} [{user_id}]", guild_name)
        await message.channel.send(f"Server name: {guild_name}\nMember count: {member_count}")
        

client.run(token)

