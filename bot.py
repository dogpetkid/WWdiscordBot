# Import all the needed libraries associated with a discord bot
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time



#NOTE Client and client are 2 distinct things

# Client is the discord connection(?)
Client = discord.Client()
# client is the command associated to the bot(?)
client = commands.Bot(command_prefix = "$")

# This is the on ready event
# When the bot is ready it will output to the chat "Bot is ready!"
@client.event
async def on_ready():
    print("Bot is ready!")

# This is the on message event
# When the bot sees a message in the chat, it will run this event
@client.event
async def on_message(message):
    if (message.content == "cookie"):
        # await makes sure the client is actually ready to send the message
        ##await client.send_message(message.channel, ":cookie:")
        await message.channel.send(":cookie:")


# This specifies the bot we are controlling by using the token of the bot
client.run("NTAxOTY0NDk0NjE3MTgyMjI5.DqmW4g.u5uaZ0ufN2Jb7nrbVinYw89UnJ8")

