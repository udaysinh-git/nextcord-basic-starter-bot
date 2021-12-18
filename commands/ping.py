from nextcord.ext import commands
import nextcord
from datetime import datetime
import nextcord, requests, json, os
import random2
from nextcord import client
from nextcord.ext import commands
import nextcord
from nextcord import *
import nextcord, requests, json, os
from nextcord.ext.commands import bot
import random2
import nextcord.ext.commands as commands
from nextcord.ui import Button, View

from nextcord import Embed




class Ping(commands.Cog):
    '''Ping Command is availabe here'''

    
    def __init__(self, bot):
        self.bot=bot

         
    @commands.command(brief='Shows the ping of the bot', description='Shows the ping of the bot')
    async def ping(self, ctx):
        responses = [ctx.author.mention, f'**Pong!** ```{round(self.bot.latency * 1000)}ms```',
                     f'Pong! {round(self.bot.latency * 1000)}ms'    ,
                     f'Pong! {round(self.bot.latency * 1000)}ms',
                     f'Pong! {round(self.bot.latency * 1000)}ms',
                     f'Pong! {round(self.bot.latency * 1000)}ms',]
        #await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')
        await ctx.send(random2.choice(responses))
        print(f'{ctx.message.author} wants to know the ping of the bot!')






def setup(bot):
    bot.add_cog(Ping(bot))
    print('Ping Commands Ready!!!')