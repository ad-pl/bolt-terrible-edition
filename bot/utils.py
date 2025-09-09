#!/usr/bin/env python3
# bot/utils.py
'''
common utilities used throughout the bot's codebase

essentially,
just a group of functions that don't belong anywhere else,
because DRY.
'''

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

def get_env_var(var: str, default: Any = None, required=True, from_dot_env=True):
  '''
  literally does what it says on the tin
  why does this need a docstring
  '''
  
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

def parse_duration(duration: str): # the return type annotations are gone now. screw you.
  '''
  parses a value like "1h30m" into seconds.
  returns None if the duration is empty (or 0)
  and returns False if the duration is invalid.

  we're NOT using regex for this.
  spark says "regex makes me have an aneurysm."
  '''

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

async def say(ctx: discord.ApplicationContext | commands.Context, msg: str, ephemeral=False):
  '''
  a wrapper around ctx.send() and ctx.respond().
  '''

  is_slash = isinstance(ctx, discord.ApplicationContext)

  if is_slash:
    await ctx.respond(msg, ephemeral=ephemeral)
  else:
    await ctx.send(msg)

async def assert_guild(ctx, guild, user):
  # TODO: rewrite this. it sucks. its bad. it barely even works.
  #       im not gonna bother writing a docstring for this.
  
  if guild is None:
    console.log(f"{user} tried to run a command where it's not supported.", "LOG")
    await say(ctx, "You can't run that command here!", ephemeral=True)
    return False
  
  return True
