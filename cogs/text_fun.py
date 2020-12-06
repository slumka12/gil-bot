import json
from time import sleep

import discord
import pyfiglet
from discord.ext import commands, tasks
from func import (bible, jsGet, listToString, make_embed, removeChar, sponge,
                  stringToList, userGrab)
from gil_bot import PREFIX

#To add:

speed = 1

class Text_Fun(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(description=f"Repeats a message\n {PREFIX}rep <number> <content>")
  async def rep(self, ctx, num=10, *, words="words"):
    for _ in range(int(num)):
        await ctx.send(words)
        sleep(speed)
  
  @commands.command(description=f"Writes a message in ASCII\n {PREFIX}ascii <words>")
  async def ascii(self, ctx, *, text="Put in words next time"):
    ascii_banner = pyfiglet.figlet_format(text)
    await ctx.send("```"+ascii_banner+"```")

  @commands.command(description=f"Puts your message in sponge case\n {PREFIX}sponge <content>")
  async def sponge(self, ctx, *, words = "Put in words next time"):
    #await ctx.message.delete()
    await ctx.send(sponge(words))

  @commands.command(description="Grabs a random bible quote")
  async def bible(self, ctx):
    b = bible()
    await ctx.send(embed=make_embed(title=b[0],description=b[1], author="God"))

  @commands.command(description=f"Registers a group or edits an existing one\n {PREFIX}groupUp <group name> <members>", aliases = ["ga","groupadd"])
  async def groupAdd(self, ctx, groupName : str, *, members):
    if "@" in groupName:
      await ctx.send(embed=make_embed(title="Missing Argument `groupName`", color=16711680,footer="Name the group something you'll remember!"))
    else:
      members = stringToList(removeChar(members,removes=["<","!","@",">"]))
      #print(members)
      mJson = jsGet("groups")
      if groupName not in mJson:
        mJson[groupName] = members
        with open ("groups.json","w") as j:
          json.dump(mJson, j, indent=2, sort_keys=True)
        await ctx.send(embed=make_embed(title=f"Group: \"{groupName}\" added", 
                description=f"Members are {listToString([i.mention for i in userGrab(self.client,mJson[groupName])],', ',' and ')}"))
      else: await ctx.send(embed=make_embed(title="Group already exists",footer="Try using another name"))

  @commands.command(description="Shows Groups You're In")
  async def groups(self, ctx, force=False):
    if force:
      if ctx.author.id not in jsGet("admo")["admin"]:
        force = False
    mJson = jsGet("groups")
    if not force: l = [i for i in mJson if str(ctx.author.id) in mJson[i]]
    else: l = [i for i in mJson]
    await ctx.send(embed=make_embed(title="Your Groups",description=listToString(l,", "," and ")))

  @commands.command(description=f"Reunites a group\n {PREFIX}groupUp <group name>", aliases = ["gu","groupup","unite"])
  async def groupUp(self, ctx, groupName, num = 1):
    mJson = jsGet("groups")
    if groupName in mJson:
      if str(ctx.author.id) in mJson[groupName]:
        await self.rep(ctx, num = num, words = f"{groupName} UNITE! {listToString([i.mention for i in userGrab(self.client,mJson[groupName])],', ',' and ')}")
      else: await ctx.send(embed=make_embed(title="Can't Gather Group",footer="You can't unite a group you're not in"))
    else: await ctx.send(embed=make_embed(title="Group Not Found",footer="Check spelling idk"))

  @commands.command(description=f"Registers a group\n {PREFIX}groupDisband <group name>", aliases = ["disband"])
  async def groupDisband(self, ctx, groupName, force = False):
    if force:
      if ctx.author.id not in jsGet("admo")["admin"]:
        force = False
    mJson = jsGet("groups")
    if str(ctx.author.id) in mJson[groupName] or force:
      removed = mJson.pop(groupName,None)
      with open("groups.json","w") as j:
        json.dump(mJson, j, indent=2, sort_keys=True)
      await ctx.send(embed = make_embed(title=f"\"{groupName}\" disbanded", 
                description=f"Members were {listToString([i.mention for i in userGrab(self.client,removed)],', ',' and ')}"))
    else: await ctx.send(embed=make_embed(title="Cannot Disband Group",footer="You can't disband a group you're not in"))
  

def setup(client):
  client.add_cog(Text_Fun(client))
