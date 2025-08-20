# bot/__main__.py

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