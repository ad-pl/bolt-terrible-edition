#!/usr/bin/env python3
# bot/constants/config.py
'''
loaded by utils.py, console.py, and bot.py

not really sure why this file is called "config" but eh
if it aint broke dont fix it

spark says:
NOTE: these constants here aren't exactly user configurable aside from prompt
      which leads me to think that i should move prompt to the .env file
      and have it be loaded by another constant file (because circular imports cant have it here)
'''

# LIBRARIES AND MODULES

from pathlib import Path

# CONSTANTS

env_path = Path(".env")

default_prefix = "."

prompt = "% "

units = {
  "d": 86400, # days
  "h": 3600,  # hours
  "m": 60,    # minutes
  "s": 1      # seconds
}