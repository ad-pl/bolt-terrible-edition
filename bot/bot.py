# bot/bot.py
'''
the bootstrapper for the bot
this file creates the bot instance, loads cogs, and starts the bot.
'''

# LIBRARIES AND MODULES

import time

## pycord

import discord
from discord.ext import commands

## pypkg

import bot.constants.base as constants
import bot.console as console
import bot.utils as utils

# INIT

token = utils.get_env_var("TOKEN", default=None, required=True, from_dot_env=True) # get token

intents = discord.Intents.default()
intents.message_content = True
# if reaction roles will be added to the bot, then intents.reactions = True

bot = commands.Bot(command_prefix=constants.prefix, intents=intents, help_command=None) # create bot instance, remove built-in help command

# FUNCTIONS

@bot.event
async def on_ready():
  '''
  event that runs when the bot connects to discord.
  '''

  setattr(bot, "start_time", time.time())
  console.log(f"Bolt is online as {bot.user}", "LOG")

@bot.event
async def on_command_error(ctx, error):
  '''
  runs on every command error.

  currently only handles CommandNotFound errors because the cogs should have their own error handling.

  KNOWN BUG:
  - if you type something like "..." then the bot will assume that
    ".." is a command and will throw a CommandNotFound error.
    why is this? because of our choice of default prefix. uhhh...
    sorry?
  '''

  if isinstance(error, commands.CommandNotFound):
    console.log(str(error), "ERROR")
    await utils.say(ctx, f"Command not found. \nRun {constants.prefix}help to see all available commands.") # is_slash is False by default

## START UP

def load_cogs():
  '''
  loads all cogs defined in constants.extensions.
  raises an exception if any cog fails to load.

  any cog that isn't in constants.extensions will NOT be loaded, so dont forget to update the tuple when adding or removing cogs.
  '''

  for ext in constants.extensions:
    try:
      bot.load_extension(ext)
      console.log(f"Loaded extension: {ext}", "DEBUG")
    except Exception as e:
      console.log(f"Failed to load extension: {ext}", "DEBUG")
      console.log(f"Exception: {e}", "DEBUG")
      raise

def start_bot():
  '''
  okay dude does this seriously need a docstring
  '''

  load_cogs()
  bot.run(token)