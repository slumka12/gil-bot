from warnings import filterwarnings

import discord
import wikipedia
from bs4 import GuessedAtParserWarning
from discord.ext import commands, tasks
from func import make_embed
from gil_bot import PREFIX

filterwarnings("ignore",category=GuessedAtParserWarning)


class Wikipedia_Grab(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(description=f"Grabs a Wikipedia Article\n {PREFIX}wiki <topic>")
  async def wiki(self, ctx, *, topic = None):
    if not topic:
      topic = wikipedia.random()
    page = wikipedia.page(title = topic)
    await ctx.send(embed=make_embed(title=page.title, 
            description=wikipedia.summary(title = topic, sentences = 2),link=page.url, 
            footer="Wikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects."))


def setup(client):
  client.add_cog(Wikipedia_Grab(client))
