#!/usr/bin/env python3
# bot/cogs/help.py
'''
handles the help commands
'''

# LIBRARIES AND MODULES

## pycord

import discord
from discord.ext import commands

## pypkg

import bot.console as console
import bot.markdown.help as help
## from bot.constants.base import prefix
import bot.utils as utils

# CLASSES

class Help(commands.Cog):
  '''
  handles the help commands
  '''

  def __init__(self, bot):
    self.bot = bot

  def fetch_help(self):
    '''
    <method>

    fetches the help markdown file, finds and replaces constants, then returns the final string.
    '''

    with open(help.help_md, "r", encoding="utf-8") as f:
      help_data = f.read()
    
    for find, replace in help.find_and_replace.items():
      help_data = help_data.replace(find, replace)
    
    return help_data

  async def _help(self, ctx):
    '''
    <_command>

    sends the help message in the channel the command was invoked in.
    '''

    user = ctx.author

    console.log(f"Help requested by {user} ({user.id})", "LOG")

    message = self.fetch_help()
    
    await utils.say(ctx, message)

  # COMMANDS

  # prefix command
  @commands.command()
  async def help(self, ctx: commands.Context):
    await self._help(ctx)

  # slash commands
  @commands.slash_command(name="help", description="send the help message.")
  async def slash_help(self, ctx: discord.ApplicationContext):
    await self._help(ctx)

# FUNCTIONS

def setup(bot):
  '''
  adds Help cog to the bot
  '''

  bot.add_cog(Help(bot))
