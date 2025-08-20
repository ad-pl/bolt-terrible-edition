# bot/console.py
# NOTE: this file is literally empty aside from log()
#       im not sure if console.log should be moved to utils.py
#       one less file is always nice but it WOULD break literally
#       every instance of console.log() which would need to be replaced with
#       utils.log() which i will never get used to

# LIBRARIES AND MODULES

import time

## pypkg

## from bot.constants import *
import bot.constants.colors as colors

# FUNCTIONS

def log(msg, level="LOG"):
  print(f"{colors.log_colors[level.upper()]}[{level.upper()}]{colors.reset_colors} [{time.asctime(time.gmtime())}] {msg}")
  # in plain english,
  # it just outputs:
  # [LOG] [current time] [message]
