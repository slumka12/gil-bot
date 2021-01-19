import random

import discord
import praw
from discord.ext import commands
from func import make_embed
from gil_bot import PREFIX


class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.rSess = praw.Reddit(client_id="wqA7c3mg7FNPXQ",
                    client_secret="Iy2LJpk8ggekoZZaag-iBXgEnnw",
                    user_agent="android:com.example.myredditapp:v1.2.3 (by u/Giruchan)")
        self.spacer = "        "

    def karmaScrape(self,user):
        redditor=self.rSess.redditor(user)
        return redditor.link_karma + redditor.comment_karma

    def post_Scrape(self,sub):
        posts=self.rSess.subreddit(sub).hot(limit=75)
        picked = random.randint(1,75)
        submissions = (x for x in posts if (not x.stickied) and ((".jpg" in x.url) or (".png" in x.url) or (".gif" in x.url)))
        for submission in submissions:
            if picked == 0:
                return [submission.title, submission.url, submission.subreddit, submission.over_18, submission.author]
            picked-=1
        
    def text_Post_Scrape(self,sub):
        posts=self.rSess.subreddit(sub).hot(limit=75)
        picked = random.randint(1,75)
        submissions = (x for x in posts if (not x.stickied) and not((".jpg" in x.url) or (".png" in x.url) or (".gif" in x.url)))
        for submission in submissions:
            if picked == 0:
                return [submission.title, submission.selftext, submission.subreddit, submission.over_18, submission.author]
            picked-=1

    def userImageScrape(self,user):
        posts=self.rSess.redditor(user).submissions.top(limit=25)
        picked = random.randint(0,25)
        submissions = (x for x in posts if (not x.stickied) and ((".jpg" in x.url) or (".png" in x.url) or (".gif" in x.url)))
        for submission in submissions:
            if picked == 0:
                return [submission.title, submission.url, submission.subreddit, submission.over_18, submission.author]
            picked-=1

    ###Commands###

    @commands.command(description=f"Gets a post off any sub\n {PREFIX}reddit <sub>",aliases=["r","memes","meme"])
    async def reddit(self, ctx, sub="dankmemes"):
        info=self.post_Scrape(sub)
        c = 5
        while (not info) and c>0:
            info=self.post_Scrape(sub)
            c-=1
        if not info: await self.redditError(ctx,sub)
        else:        
            if info[3]==True and ctx.channel.is_nsfw()==False:
                await ctx.send(embed=make_embed(title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
            else:
                await ctx.send(embed=make_embed(title=info[0],image=info[1],footer=f"Posted on r/{info[2]} by u/{info[4]}"))


    @commands.command(description=f"Gets a post from any user\n {PREFIX}redditor <user>")
    async def redditor(self, ctx, user):
        info=self.userImageScrape(user)
        c = 5
        while (not info) and c>5:
            info=self.userImageScrape(user)
            c-=1
        if not info: await self.redditError(ctx,user)
        else:
            if info[3]==True and ctx.channel.is_nsfw()==False:
                await ctx.send(embed=make_embed(title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
            else:
                await ctx.send(embed=make_embed(title=info[0],image=info[1],footer=f"Posted on r/{info[2]} by u/{info[4]}"))

    @commands.command(description=f"Gets text posts\n {PREFIX}textpost <sub>",aliases=["t","pasta"])
    async def textpost(self, ctx, sub="copypasta"):
        c = 5
        info=self.text_Post_Scrape(sub)
        while (not info) and c>0:
            info=self.post_Scrape(sub)
            c-=1
        if not info: await self.redditError(ctx,sub)
        else:
            if info[3]==True and ctx.channel.is_nsfw()==False:
                await ctx.send(embed=make_embed(title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
            else:
                await ctx.send(embed=make_embed(title=info[0],description=info[1],footer=f"Posted on r/{info[2]} by u/{info[4]}"))

    @commands.command(description="Reddit postType error", hidden=True)
    async def redditError(self,ctx,sub):
        await ctx.send(embed=make_embed(title="Something went wrong",
                                                description=f"Requested subreddit: r/{sub} has too many of the wrong post type for the bot to filter",
                                                footer="Maybe try again with the opposite command?"))

    @commands.command(description=f"Grabs a user's total karma\n {PREFIX}karma <user>",aliases=["k"])
    async def karma(self,ctx,user):
        await ctx.send(f"{user.capitalize()} has {self.karmaScrape(user)} karma")


def setup(client):
  client.add_cog(Reddit(client))
