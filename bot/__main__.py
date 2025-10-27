#!/usr/bin/env python3

# bot/__main__.py
'''
main entry point

recommended to use this file instead of running bot.start_bot() directly
NOTE: the above line is not true.
'''

# SAFEGUARDS

def dir_safeguard():
  '''
  simple check to see if you're running the bot from the repo root.
  NOTE: because the safeguard only runs in this file, people can easily just run `bot.start_bot()` directly
        and see the effects of running bolt outside the root. (spoiler: it will crash.)
  
  NOTE: yeah no this is useless. this safeguard is pointless because of how python PATHs work, will remove later.
  '''

  from pathlib import Path

  cwd = Path.cwd()
  root = Path(__file__).resolve().parent.parent # in other words, the parent directory of the directory that __file__ is in

  if cwd != root:
    raise RuntimeError(f"Never run Bolt from outside this directory: {root}\nYou're in the {cwd} directory.")

# LIBRARIES AND MODULES

## pypkg

from bot.constants.colors import allow_colors
import bot.bot as bot
import bot.console as console

# FUNCTIONS

def main():
  '''
  le bootstrapper
  '''

  dir_safeguard()
  
  try:
    console.log("Starting Bolt...", "LOG")

    if not allow_colors:
      console.log("You don't have `colorama` installed. If you want colored logs, run `pip install colorama`.", "WARN")

    bot.start_bot()

  except Exception as e:
    console.log(f"Something happened. exception: {e}", "FATAL")

  except KeyboardInterrupt:
    console.log(f"Bolt shutting down...", "LOG")

# START UP

if __name__ == "__main__":
  main()