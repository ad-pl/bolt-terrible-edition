#!/usr/bin/env python3
# bot/console.py
'''
it just logs things.
not sure what else to say.
'''

# NOTE: this file is literally empty aside from log()
#       im not sure if console.log should be moved to utils.py
#       one less file is always nice but it WOULD break literally
#       every instance of console.log() which would need to be replaced with
#       utils.log() which i will never get used to

# LIBRARIES AND MODULES

import time # TODO: replace with datetime

# NOTE: yes we are not using logging
#       we are literally just printing to stdout
#       there is no need to make things more complicated
#       as PEP 20 says, "Simple is better than complex."

## pypkg

## from bot.constants import *
import bot.constants.colors as colors
import bot.constants.config as config

# FUNCTIONS

def log(msg, level="LOG"):
  '''
  print wrapper that does the hard logging stuff for us.
  '''

  level = level.upper()

  level_str = f"{colors.log_colors.get(level, '')}[{level}]{colors.reset_colors}"
  time_str = f"[{time.asctime(time.gmtime())}]" # not local time because timezones are annoying
  full = f"{level_str} {time_str} {msg}"

  print(full)
  