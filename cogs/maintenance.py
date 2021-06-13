import datetime
import json
from os import listdir
from random import choice, randint
from time import sleep

import discord
from discord.ext import commands, tasks
from func import jsGet, make_embed
from gil_bot import PREFIX, botID, me
from lists import die, ilan, playing


class Maintenance(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.tStat = None
    self.randEvent = 100
    self.eStat = True

###STATUS LOOP###

  @tasks.loop(hours=4)
  async def stat(self):
    new = str(choice(playing))
    if new != self.tStat: 
      await self.client.change_presence(activity=discord.Game(name=new))
      #print(f"{self.client.user} changed status")
      self.tStat = new
    else:
      self.stat.restart()

  @commands.command(description = "Manually Changes Status Message and resets loop", hidden = True, aliases=["stat"])
  @commands.is_owner()
  async def status(self, ctx, *, new=None):
    if new == "start": self.stat.start()
    elif new: await self.client.change_presence(activity=discord.Game(name=str(new)))
    else: self.stat.restart()

  @commands.command(description = "Checks Time Till Next Iteration of Loop", hidden = True, aliases=["loopnext","lN"])
  @commands.is_owner()
  async def loopNext(self, ctx):
    ne = self.stat.next_iteration.replace(tzinfo=datetime.timezone.utc) - datetime.datetime.now(datetime.timezone.utc)
    #print(ne)
    await ctx.send(embed=make_embed(title=f"{ne.seconds//3600} Hour(s) {int(round((ne.seconds/60)%60, 0))} Minute(s) Until Next Status Loop"))

  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.client.user} is online")
    self.stat.start()
    #await self.client.change_presence(activity=discord.Game(name="Testing Mode: ON"))

###ON MESSAGE SHIT###

  @commands.Cog.listener()
  async def on_message(self, message):
    if (message.author.id != botID) and (self.randEvent != -1):
      if "ilan" in message.content.lower():
        if randint(1,self.randEvent)==1:
            await message.channel.send(f"Guys remember that time {choice(ilan)}")

  @commands.command(description=f"Controls random text responses. Lower number = more spam (-1 to cancel all) \n {PREFIX}rate", hidden = True)
  @commands.is_owner()
  async def rate(self, ctx, number=None):
    if number:
      if not number.isdigit() and (number != "-1") : number = 100
      self.randEvent = int(number)
      await ctx.send(embed=make_embed(title="Rate Changed",description=f"Random events are now 1 in {self.randEvent}"))
    else: await ctx.send(embed=make_embed(title=f"Random Event Rate is currently 1 in {self.randEvent}"))

###ERRORS###

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    #if self.eStat:
    eType = type(error)
    #print(eType)
    eFoot = "This is likely the fault of the bots creator. DM him to let him know!"
    eColor = 16711680
    if eType is commands.CommandInvokeError:
      await ctx.send(embed=make_embed(title="Command Invoke Error",description=f"Details are: `{error.original}`", color=eColor, footer=eFoot))
    # elif eType is commands.CommandNotFound: #took it out bc it was being annoying as fucc
    #   await ctx.send(embed=make_embed(title="Command Not Found", color=eColor,footer=eFoot))
    elif eType is commands.MissingRequiredArgument:
      await ctx.send(embed=make_embed(title=f"Missing argument: `{error.param}`", color=eColor, footer=eFoot))
    elif eType is commands.TooManyArguments:
      await ctx.send(embed=make_embed(title=f"You used too many arguments", color=eColor, footer=eFoot))
    elif eType in [commands.UserNotFound,commands.MemberNotFound]:
      await ctx.send(embed=make_embed(title=f"`{error.argument}` was not found", color=eColor, footer=eFoot))
    elif eType is commands.MissingPermissions:
      await ctx.send(embed=make_embed(title="Must have following permission(s): "+ ", ".join([f"`{perm}`" for perm in error.missing_perms]), color=eColor, footer=eFoot))
    elif eType is commands.BotMissingPermissions:
      await ctx.send(embed=make_embed(title="I must have following permission(s): "+ ", ".join([f"`{perm}`" for perm in error.missing_perms]), color=eColor, footer=eFoot))
    elif eType is commands.NotOwner:
      await ctx.send(embed=make_embed(title=f"You aren't bot owner", color=eColor, footer=eFoot))
    else: await ctx.send(embed=make_embed(title="Something went wrong", color=eColor, footer=eFoot))

  @commands.command(description="Test", hidden = True)
  async def test(self, ctx, *, word):
    await ctx.send(f"{word} b")
 
  @commands.command(description="Die",aliases=["die"], hidden = True)
  @commands.is_owner()
  async def kill(self, ctx):
    await ctx.send(f"{choice(die)}", delete_after=2.5)
    quit()
  
  @commands.command(description="Reloads Cogs",aliases=["unload"], hidden = True)
  @commands.is_owner()
  async def reload(self, ctx):
    await ctx.send("Reloading Cogs", delete_after=2.5)
    self.stat.cancel()
    for filename in listdir('./cogs'):
      if filename.endswith('.py'):
        self.client.reload_extension(f'cogs.{filename[:-3]}')
    await ctx.send("Done!", delete_after=2.5)



def setup(client):
  client.add_cog(Maintenance(client))
  #print("setup")

#def teardown(client):
  #print("teardown")
