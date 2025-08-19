# bot/constants/config.py

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