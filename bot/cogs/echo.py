#!/usr/bin/env python3
# bot/cogs/echo.py
'''
handles the echo commands
'''

# LIBRARIES AND MODULES

## pycord

import discord
from discord.ext import commands

## pypkg

import bot.console as console
import bot.utils as utils

# CLASSES

class Echo(commands.Cog):
  '''
  handles the echo commands
  '''

  def __init__(self, bot):
    self.bot = bot
  
  async def _echo(self, ctx, msg=None):
    '''
    <_command>

    says a message provided by the user in the channel the command was invoked in.
    '''

    user = ctx.author

    console.log(f"{user} requested an echo.", "LOG")

    if msg is None:
      console.log("There is nothing to echo, returning.", "INFO")
      await utils.say(ctx, "There's nothing to echo.", ephemeral=True)
      return
    
    console.log(f"To be echoed: {msg}", "INFO")
    await utils.say(ctx, msg)
  
  # COMMANDS

  # prefix command
  @commands.command()
  async def echo(self, ctx: commands.Context, *, msg=None):
    await self._echo(ctx, msg)
  
  # slash command
  @commands.slash_command(name="echo", description="make the bot say something!")
  @discord.option("message", description="what to say", type=str)
  async def slash_echo(self, ctx: discord.ApplicationContext, msg=None):
    await self._echo(ctx, msg)

# FUNCTIONS

def setup(bot):
  '''
  adds Echo cog to the bot
  '''

  bot.add_cog(Echo(bot))