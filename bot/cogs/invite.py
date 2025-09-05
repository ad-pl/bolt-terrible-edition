#!/usr/bin/env python3
# bot/cogs/invite.py
'''
handles the invite commands
'''

# LIBRARIES AND MODULES

## pycord

import discord
from discord.ext import commands

## pypkg

import bot.utils as utils
import bot.console as console

# CLASSES

class Invite(commands.Cog):
  '''
  handles the invite commands
  '''

  def __init__(self, bot):
    self.bot = bot
  
  async def _invite(self, ctx):
    '''
    <_command>

    sends an invite link to the bot's support server and a link to add the bot to a server. (of course its a redirect from my website)
    '''

    user = ctx.author
    is_slash = isinstance(ctx, discord.ApplicationContext)

    # TODO: put this in a markdown file
    message = """
Add Bolt to your server!
https://sparkhere-sys.github.io/bolt

Support server:
https://discord.gg/hF6mgCE3gT
    """

    console.log(f"{user} requested an invite link.", "LOG")
    await utils.say(ctx, message, is_slash=is_slash)
  
  # COMMANDS

  @commands.command()
  async def invite(self, ctx: commands.Context):
    await self._invite(ctx)
  
  @commands.slash_command(name="invite", description="invite the bot to your server!")
  async def slash_invite(self, ctx: discord.ApplicationContext):
    await self._invite(ctx)

# FUNCTIONS

def setup(bot):
  '''
  adds Invite cog to the bot
  '''

  bot.add_cog(Invite(bot))