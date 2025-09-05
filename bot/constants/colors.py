#!/usr/bin/env python3
# bot/constants/colors.py
'''
used by console.py to color log output
'''

# LIBRARIES AND MODULES

try:
  from colorama import init, Fore, Style
  allow_colors = True
  init()
except ImportError:
  allow_colors = False

# COLORS

log_colors = {
  "LOG": Fore.WHITE if allow_colors else '',
  "DEBUG": Fore.CYAN if allow_colors else '',
  "INFO": Fore.BLUE if allow_colors else '',
  "WARN": Fore.YELLOW if allow_colors else '',
  "ERROR": Fore.RED if allow_colors else '',
  "FATAL": (Fore.RED + Style.BRIGHT) if allow_colors else ''
}

reset_colors = Style.RESET_ALL if allow_colors else ''