# bot/cogs/moderation/ban.py

# LIBRARIES AND MODULES

## pycord

import discord
from discord.ext import commands

## pypkg

from bot.cogs.moderation.base import Base

# CLASSES

class Ban(Base):
  def __init__(self, bot):
    super().__init__(bot)
    self.config(ban=True)
  
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx: commands.Context, target: discord.Member, *, reason=None):
    await self.action(ctx, target, "ban", reason)
  
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx: commands.Context, target: discord.User, *, reason=None):
    self.config(ban=True, is_un=True) # reconfiguring for an unban
    await self.action(ctx, target, "unban", reason)
  
  @commands.slash_command(name="ban", description="ban a user")
  @commands.has_permissions(ban_members=True)
  async def slash_ban(self, ctx: discord.ApplicationContext, target: discord.Member, reason: str | None = None):
    await self.action(ctx, target, "ban", reason) # no need for is_slash=True, that is determined automatically now

  @commands.slash_command(name="unban", description="unban a previously banned user")
  @commands.has_permissions(ban_members=True)
  async def slash_unban(self, ctx: discord.ApplicationContext, target: discord.User, reason: str | None = None):
    self.config(ban=True, is_un=True) # ditto (see unban())
    await self.action(ctx, target, "unban", reason) # ditto (see slash_ban())

# FUNCTIONS

def setup(bot):
  bot.add_cog(Ban(bot))