#!/usr/bin/env python3
'''
NOTE: prefix is located in base.py
      because it is required for the bot to start.
      every env key that isn't required however will be
      located here.
      this means that configs and such will belong in this file and
      will be loaded from the .env file.
'''

# LIBRARIES AND MODULES

## pylib

from bot.utils import get_env_var

# ENV KEYS

prompt = get_env_var("CONSOLE_PROMPT", "% ", required=False, from_dot_env=True)