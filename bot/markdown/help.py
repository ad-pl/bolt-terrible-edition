# bot/constants/help_md.py
'''
paired with bot/markdown/help.md
'''

# LIBRARIES AND MODULES

from pathlib import Path
from bot.constants.base import prefix

# PATHS

help_md = Path("bot/markdown/help.md")

# CONSTANTS

_support = "https://discord.gg/hF6mgCE3gT"
_repo_link = "https://github.com/sparkhere-sys/bolt"

find_and_replace = {
  # "find": "replace"
  "{prefix}": prefix,
  "{support}": f"<{{_support}}>",
  "{repo}": f"Bolt is open source! You can find the code at <{_repo_link}>",
}
