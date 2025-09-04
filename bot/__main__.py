# bot/__main__.py
'''
main entry point

recommended to use this file instead of running bot.start_bot() directly

KNOWN BUG:
- if you run this OUTSIDE of the repository root, (the parent directory of bot/)
  bolt will trip up on the paths because i never added any safeguards for that and never will,
  and you'll get FileNotFoundErrors.
'''

# LIBRARIES AND MODULES

## pypkg

from bot.constants.colors import allow_colors
import bot.bot as bot
import bot.console as console

# FUNCTIONS

def main():
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