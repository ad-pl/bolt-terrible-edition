# bot/cogs/moderation/base.py

# LIBRARIES AND MODULES

from datetime import timedelta # for use with timeout

## pycord

import discord
from discord.ext import commands

## pypkg

from bot.constants.moderation import *
import bot.console as console
import bot.utils as utils

# CLASSES

class Base(commands.Cog): # not actually a cog. it just inherits from commands.Cog
  def __init__(self, bot):
    self.bot = bot

  def config(self, **kwargs):
    """
    was it a good idea to use **kwargs and not document WHAT those kwargs are?
    probably not.
    """
  
    self.timeout = kwargs.get("timeout", False)
    self.ban = kwargs.get("ban", False)
    self.kick = kwargs.get("kick", False)

    self.is_un = kwargs.get("is_un", False) # genuinely one of the dumbest names for a variable ever but it works (i hope)
    self.use_duration = True if (self.timeout) and (not self.is_un) else False # temporary bans haven't been added yet and will be pretty hard to add

    if self.timeout:
      self.verb = "mute"
      self.verb_past = "muted" if not self.is_un else "unmuted"
      return

    if self.ban:
      self.verb = "ban"
      self.verb_past = "banned" if not self.is_un else "unbanned"
      return
    
    if self.kick:
      self.verb = "kick"
      self.verb_past = "kicked" if not self.is_un else "unkicked" # i know that unkicking is impossible, but my point still stands.
      return
  
  def check_for_permissions(self, perm, user, _perm_map):
    if not perm:
      return False # early return
    
    if not perm in _perm_map:
      return False # ditto
    
    if getattr(user.guild_permissions, _perm_map[perm], False):
      return True # ditto
    
    return False

  async def action(self, ctx, target, action_type, reason=None, duration="30m"):
    user = ctx.author
    reason = reason or "None provided."

    is_slash = isinstance(ctx, discord.ApplicationContext)

    # that's a lot of console.log()s
    console.log(f"An action has been requested.", "LOG")
    console.log(f"Action type: {action_type}", "INFO")
    console.log(f"Target: {target} ({target.id})", "INFO")
    console.log(f"Requested by: {user} ({user.id})", "INFO")
    console.log(f"Reason: {reason}", "INFO")
    console.log(f"Duration: {duration}", "INFO")

    # time for the checks and early returns!!!!

    if not await utils.assert_guild(ctx, guild=ctx.guild, user=user, is_slash=is_slash):
      return
    
    if target == user:
      await utils.say(ctx, f"You can't {self.verb} yourself!", is_slash=is_slash, ephemeral=True)
      console.log(f"{user} tried to {self.verb} themselves.", "LOG")
      return
    
    if not self.check_for_permissions(action_type, user, _perm_map=perm_map if not self.is_un else un_perm_map):
      await utils.say(ctx, f"You don't have permission to {self.verb} members.", is_slash=is_slash, ephemeral=True)
      console.log(f"{user} tried to {self.verb} {target} but doesn't have permission.", "LOG")
      return
    
    # now we parse the duration
    
    if self.use_duration:
      seconds = utils.parse_duration(duration)
      
      if not seconds:
        await utils.say(ctx, "Invalid duration format. Try `3d`, `1h`, `30m`, `45s`", is_slash=is_slash, ephemeral=True)
        return
      
      # if seconds < 0 check is not required. parse_duration() will just kill itself if it sees a negative number anyway

      if seconds >= 2419200: # as in, 28 days.
        if self.ban:
          seconds = 0 # anything larger than 28 days and discord will die so we just make it a perma ban
        elif self.timeout: # made this into an elif just to sanity check
          await utils.say(ctx, "Dude you can't even mute someone for that long.", is_slash=is_slash, ephemeral=True)
          return
      
    # NOW we do the action. finally.

    try:
      match action_type:
        # not is_un
        case "ban":
          await target.ban(reason=reason)
        
        case "timeout":
          await target.timeout_for(timedelta(seconds=seconds), reason=reason)
        
        case "kick":
          await target.kick(reason=reason)
        
        # is_un
        case "unban":
          await ctx.guild.unban(target, reason=reason)

        case "untimeout":
          await target.remove_timeout(reason=reason)

        # literally anything else
        case _:
          raise ValueError("that action_type doesn't exist dude.")
    
    except discord.Forbidden:
      console.log(f"Failed to {self.verb} {target}, permission denied.", "ERROR")
      await utils.say(ctx, f"I don't have permission to {self.verb} that user.", is_slash=is_slash, ephemeral=True)
      return
    
    except discord.HTTPException:
      console.log(f"Failed to {self.verb} {target}, HTTPException raised.", "ERROR")
      await utils.say(ctx, f"Something went wrong while trying to {self.verb} that user.", is_slash=is_slash, ephemeral=True)
      return
    
    except Exception as e:
      console.log(f"Exception raised: {e}", "ERROR")
      await utils.say(ctx, "Something went wrong in the bot's code. Try again later.", is_slash=is_slash, ephemeral=True)
      return
    
    console.log(f"{user} {self.verb_past} {target}{(' for ' + duration) if self.use_duration else ''} for: {reason}", "LOG")

    success_message = f"{self.verb_past.capitalize()} {target.mention}{(' for ' + duration) if self.use_duration else ''}. \nReason: {reason}"
    await utils.say(ctx, success_message, is_slash=is_slash)