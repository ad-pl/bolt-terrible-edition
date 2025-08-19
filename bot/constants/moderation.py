# bot/constants/moderation.py

perm_map = {
  "ban": "ban_members",
  "kick": "kick_members",
  "timeout": "moderate_members",
}

un_perm_map = {
  "unban": "ban_members",
  "untimeout": "moderate_members",
}