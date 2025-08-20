# bot/utils.py

# LIBRARIES AND MODULES

from typing import Any
from dotenv import load_dotenv
import os

## pycord

import discord
from discord.ext import commands

## pypkg

import bot.console as console
from bot.constants.config import env_path, units

# FUNCTIONS

def get_env_var(var: str, default: Any, required=True, from_dot_env=True):
  if from_dot_env:
    if not env_path.exists():
      console.log(f"No .env file found.", "WARN" if not required else "FATAL")
      if required:
        raise FileNotFoundError(f"fatal: No .env file found, please create one including {var}")
      else:
        console.log(f"Using default value for {var}: {default}", "DEBUG")
        return default
    
    load_dotenv(dotenv_path=env_path)

  val = os.getenv(var, default)
  if val is None and required:
    console.log(f"Required variable ({var}) not found in .env file.", "FATAL")
    raise ValueError(f"fatal: Required variable ({var}) not found in .env file.")
    
  return val

def parse_duration(duration: str) -> int | bool | None: # the type annotations are insane on this one
  duration = duration.strip().lower()

  if not duration:
    return None
  
  total_seconds = 0
  num = ''

  for char in duration:
    if char.isdigit():
      num += char
    elif char in units:
      if not num:
        return False # meaning invalid
      
      total_seconds += int(num) * units[char]
      num = ''

  return total_seconds if total_seconds > 0 else False

async def say(ctx: discord.ApplicationContext | commands.Context, msg: str, is_slash=False, ephemeral=False):
  if is_slash and isinstance(ctx, discord.ApplicationContext): # just in case
    await ctx.respond(msg, ephemeral=ephemeral)
  else:
    await ctx.send(msg)

async def assert_guild(ctx, guild, user, is_slash=False):
  # TODO: rewrite this
  if guild is None:
    console.log(f"{user} tried to run a command where it's not supported.", "LOG")
    await say(ctx, "You can't run that command here!", is_slash=is_slash, ephemeral=True)
    return False
  
  return True
