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

# FUNCTIONS

def log(msg, level="LOG", after_console_start=True):
  '''
  print wrapper that does the hard logging stuff for us.
  '''

  print(f"{colors.log_colors[level.upper()]}[{level.upper()}]{colors.reset_colors} [{time.asctime(time.gmtime())}] {msg}")
  if not after_console_start:
    print("% ", end="", flush=True) # reprint the prompt created by the console loop in bot.py  
  