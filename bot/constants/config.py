# bot/constants/config.py
'''
loaded by utils.py

not really sure why this file is called "config" but eh
if it aint broke dont fix it
'''

# LIBRARIES AND MODULES

from pathlib import Path

# CONSTANTS

env_path = Path(".env")

default_prefix = "."

units = {
  "d": 86400, # days
  "h": 3600,  # hours
  "m": 60,    # minutes
  "s": 1      # seconds
}