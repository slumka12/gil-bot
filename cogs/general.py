import json

import discord
from discord.ext import commands, tasks
from func import jsGet, listToString, mailSend, make_embed
from gil_bot import PREFIX

#To add:
##Guilds, clear(clean/sift), kick, ban

class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(description=f"Clears Member Messages or Just All of Them\n {PREFIX}clean <number> <mention>")
  @commands.has_permissions(manage_messages=True)
  async def clean(self, ctx, num = 6, member : discord.Member = None):
    def is_them(m):
        return m.author == member
    await ctx.message.delete()
    if member:
      deleted = await ctx.channel.purge(limit=int(num), check=is_them)
      await ctx.channel.send(f"Deleted {len(deleted)} message(s)", delete_after=2.5)
    else:
      deleted = await ctx.channel.purge(limit=int(num)+1)
      await ctx.channel.send(f"Deleted {len(deleted)} message(s)", delete_after=2.5)

  @commands.command(description=f"Don't Worry About It\n {PREFIX}clean <number> <mention>", hidden = True)
  async def void(self, ctx, num = 6, member : discord.Member = None):
    if ctx.author.id in jsGet("admo")["admin"]:
      await self.clean(ctx, num, member)

  @commands.command(description="Checks joined servers and or leaves them", aliases=["guild"])
  async def guilds(self, ctx, idk="0"):
    gList=[]
    async for guild in self.client.fetch_guilds(limit=150):
        if (guild.id==int(idk)) and (ctx.author.id in jsGet("admo")["admin"]):
            await guild.leave()
            gList.append(f"I left `{guild.name}` (id {guild.id})")
        else:
            gList.append(f"`{guild.name}`: {guild.id}")
    gList.sort()
    if idk == "-1":
      sub=f"Your guild list, {ctx.author}"
      body=listToString(gList,separator="\n")
      mailSend(sub, body)
      msg = await ctx.send("Sent!")
      await msg.delete(delay=2.5)
    else: await ctx.send(embed=make_embed(title="Servers I'm In", description=listToString(gList, separator="\n")))

  @commands.command(description=f"Kick someone\n {PREFIX}kick <mention> <reason>")
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} kicked because: `{reason}`')

  @commands.command(description=f"Ban someone\n {PREFIX}ban <mention> <reason>")
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} kicked because: `{reason}`')

  @commands.command(description="Send the invite link")
  async def invite(self, ctx):
    await ctx.send(embed=make_embed(title="Invite me to your server!",link="https://discord.com/api/oauth2/authorize?client_id=702143271144783904&permissions=8&scope=bot"))

def setup(client):
  client.add_cog(General(client))
