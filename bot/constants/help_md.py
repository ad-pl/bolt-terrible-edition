# bot/constants/help_md.py

# LIBRARIES AND MODULES

from pathlib import Path
from bot.constants.base import prefix

# PATHS

help_md = Path("bot/constants/help.md")

# CONSTANTS

find_and_replace = {
  # "find": "replace"
  "{prefix}": prefix,
  "{support}": "https://discord.gg/hF6mgCE3gT",
  "{repo}": "Bolt is open source! You can find the code at https://github.com/sparkhere-sys/bolt",
}