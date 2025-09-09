#!/usr/bin/env python3
# bot/bot.py
'''
the bootstrapper for the bot
this file creates the bot instance, loads cogs, and starts the bot.
'''

# LIBRARIES AND MODULES

import time
import threading
import asyncio
import sys

## pycord

import discord
from discord.ext import commands

## pypkg

import bot.constants.base as constants
import bot.console as console
import bot.utils as utils
import bot.constants.env as env

# INIT

token = utils.get_env_var("TOKEN", default=None, required=True, from_dot_env=True) # get token

intents = discord.Intents.default()
intents.message_content = True
# if reaction roles will be added to the bot, then intents.reactions = True

bot = commands.Bot(command_prefix=constants.prefix, intents=intents, help_command=None) # create bot instance, remove built-in help command

# FUNCTIONS

def start_console():
  '''
  starts the bot console.
  '''

  def console_loop():
    '''
    basically
    bolt's version of a REPL
    except not really its more of a CLI
    '''

    while True:
      try:
        cmd = input(env.prompt)
        cmd = cmd.lower().strip()
        match cmd:
          case ("exit" | "quit" | "shutdown"):
            console.log("Shutting down...")
            asyncio.run_coroutine_threadsafe(bot.close(), bot.loop)
            sys.exit(0)

          case ("reload" | "restart"):
            console.log("Reloading cogs...", "LOG")
            load_cogs(reload=True, reraise=False)
            console.log("Done.", "LOG")

          case _:
            console.log(f"Unknown command: {cmd}")

      except Exception as e:
        console.log(f"exception caught in console loop: {e}", "ERROR")
        continue

  threading.Thread(target=console_loop, daemon=True).start()

## EVENTS

@bot.event
async def on_ready():
  '''
  event that runs when the bot connects to discord.
  '''

  setattr(bot, "start_time", time.time())
  console.log(f"Bolt is online as {bot.user}", "LOG", after_console_start=True)
  start_console()

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
    console.log(str(error), "ERROR") # after_console_start is irrelevant here
    await utils.say(ctx, f"Command not found. \nRun {constants.prefix}help to see all available commands.") # is_slash is False by default

## START UP

def load_cogs(reload=False, reraise=True):
  '''
  loads all cogs defined in constants.extensions.
  raises an exception if any cog fails to load.

  any cog that isn't in constants.extensions will NOT be loaded, so dont forget to update the tuple when adding or removing cogs.
  '''

  for ext in constants.extensions:
    try:
      if reload:
        bot.reload_extension(ext)
        console.log(f"Reloaded extension: {ext}", "DEBUG") # after_console_start is irrelevant here, the console should be started when this function is called with reload=True
        continue

      bot.load_extension(ext)
      console.log(f"Loaded extension: {ext}", "DEBUG", after_console_start=True)
    except Exception as e:
      console.log(f"Failed to load extension: {ext}", "DEBUG")
      console.log(f"Exception: {e}", "DEBUG")
      if reraise:
        raise

def start_bot():
  '''
  okay dude does this seriously need a docstring
  '''

  load_cogs()
  bot.run(token)