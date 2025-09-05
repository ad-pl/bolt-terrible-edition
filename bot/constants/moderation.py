#!/usr/bin/env python3
# bot/constants/moderation.py
'''
permission mappings for moderation actions

used by class Base in bot/cogs/moderation/base.py to check permissions
'''

# CONSTANTS

perm_map = {
  "ban": "ban_members",
  "kick": "kick_members",
  "timeout": "moderate_members",
}

un_perm_map = {
  "unban": "ban_members",
  "untimeout": "moderate_members",
}