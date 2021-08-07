from auctionTypes import AuctionTypes
from secret import *
import discord
from discord import message
from discord import channel

client = discord.Client()
auction_channel = ""
auction_game = ""
bidders = {}
teams = []
game_started = []
game_ended = []
rtms = 0
purse = {}
maximum_players = 0
total_purse = {}
players_bought = {}

auctiontypes = AuctionTypes()


@client.event
async def on_ready():
    """[When the bot is ready]
    """
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    """[When there is a new message in the server]

    Args:
        message ([str]): [reads the message and sends the appropriate response]
    """

    if message.author == client.user:
        # if the message is of bots
        return

    if message.content.startswith("!auc"):
        # if the message is command to the bot
        command = message.content.split(" ")
        command = [i for i in command if i]
        command = command[1:]

        if (len(command) == 1) and (command[0] == "games"):
            # if user requests games that are available
            await message.channel.send(auctiontypes.games)

        if (len(command) == 1) and (command[0] == "set"):
            # setting an auction game
            await message.channel.send("game purse number_of_teams min_bid maximum_players_per_team")

client.run(bot_token)
