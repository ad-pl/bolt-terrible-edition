# bot/cogs/help.py
# TODO: add docstrings

# LIBRARIES AND MODULES

## pycord

import discord
from discord.ext import commands

## pypkg

import bot.console as console
import bot.constants.help_md as help_md
## from bot.constants.base import prefix
import bot.utils as utils

# CLASSES

class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  def fetch_help(self):
    with open(help_md.help_md, "r", encoding="utf-8") as f:
      help_data = f.read()
    
    for find, replace in help_md.find_and_replace.items():
      help_data = help_data.replace(find, replace)
    
    return help_data

  async def _help(self, ctx):
    user = ctx.author
    is_slash = isinstance(ctx, discord.ApplicationContext)

    console.log(f"Help requested by {user} ({user.id})", "LOG")

    message = self.fetch_help()
    
    await utils.say(ctx, message, is_slash=is_slash)

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
  bot.add_cog(Help(bot))
