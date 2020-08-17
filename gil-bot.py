import discord
from discord.ext import commands,tasks
import random
import redditGrab
import time
import datetime
##import sys
import lists
import func
import AdMo
import botMail

me=382987612736192512
botID=702143271144783904
flics=264808033220165632

def notBot(user):
    if user!=702143271144783904:
        return True
    else:
        return False

def notMe(user):
    if user!=382987612736192512:
        return True
    else:
        return False   

counted=["fuck","shit","pog","wm?"]

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    stat.start()
    print('{0.user}'.format(client)+" is online")
    #await client.change_presence(activity=discord.Game(name=str(random.choice(lists.playing)),url='https://www.pornhub.com'))

@tasks.loop(hours=4)
async def stat():
    print('{0.user}'.format(client)+" changed status")
    await client.change_presence(activity=discord.Game(name=str(random.choice(lists.playing)),url='https://www.pornhub.com'))


##    try:
##        profpic=random.choice(lists.prof)
##        print(profpic)
##        await client.user.edit(avatar=profpic)
##    except:
##        print('Couldn\'t change pfp')
    
#####Stuff
    
def make_embed(ctx, title=None, description=None, color=None, author=None, image=None, link=None, footer=None):
    if not color: color = random.randint(0, 0xffffff)
    embed = discord.Embed(
        title=title,
        url=link,
        description=description,
        color=color
    )
    if author: embed.set_author(name=author)
    if image: embed.set_image(url=image)
    if footer: embed.set_footer(text=footer)
    else: embed.set_footer(text=str(datetime.datetime.now()).split('.')[0])
    return embed

#####Events

@client.event
async def on_message(message):
    #print(message.author)
    if message.author.id == 695109998715469825:
        return await message.channel.send("Hello fellow bot")
    if "turtle" in message.content.lower():
        if notBot(message.author.id):
            await message.channel.send("We don't say that name in this house")
    if ("superhot" in message.content.lower())or("super hot" in message.content.lower()):
        if notBot(message.author.id):
            for i in range(4):
                await message.channel.send("SUPER")
                time.sleep(.5)
                await message.channel.send("HOT")
                time.sleep(.75)
    if any(ele in (message.content.lower()) for ele in lists.swears):
        if notBot(message.author.id):
            if random.randint(0,100)==69:
                await message.channel.send("Woah there. Watch your language.")
    if any(word in message.content.lower() for word in counted):
        if notBot(message.author.id):
            for i in counted:
                if i in message.content.lower():
                    num=func.phraseNum(message.content.lower(),i)
                    func.wordAdd(str(message.author.id),i,num)
    if "ilan" in message.content.lower():
        if notBot(message.author.id):
            await message.channel.send(f"Guys remember that time {random.choice(lists.ilan)}")
    if "delyeet" in message.content.lower():
        if notBot(message.author.id):
            await message.delete()
    if message.author.id==462885213215916034:
        if random.randint(1,100)==69:
            await message.channel.send('Shut up Frog.')
        #await message.delete()
    if message.author.id in AdMo.mocking:
        await message.channel.send(func.sponge(message.content))
    if True==True:
        await client.process_commands(message)


##@client.event
##async def on_reaction_add(reaction,user):
##    if str(user.id)!= "702143271144783904":
##        channel = reaction.message.channel
##        message1 = await channel.send("test")
##        await message1.add_reaction("🅱")

#####Commands
        
client.remove_command("help")

@client.command()
async def help(ctx, com=None):
    if not com:
        listcom = list(client.commands)
        tempCom=[]
        commands = ''
        for command in listcom:
            if command.hidden==True:
                continue
            tempCom.append(f'{command}')
        tempCom=sorted(tempCom,key=str.lower)
        for command in tempCom:
            commands+=f'.{command}\n'
        #commands=sorted(commands,key=str.lower)
        embed = make_embed(ctx,
            title='Commands',
            description=commands+''
        )
        await ctx.send(embed=embed)
    elif com != 'help':
        try:
            comm = client.get_command(com)
            alia=f" \nAliases: {comm.aliases}"
            if comm.aliases==[]:
                alia=""
            embed = make_embed(ctx,
                title='.'+com,
                description=(comm.description+alia),
                #footer=str(datetime.datetime.now()).split('.')[0]
            )
            await ctx.send(embed=embed)
        except:
            await ctx.send('Couldn\'t get command')

@client.command()
async def test(ctx):
    pass

@client.command(description="Boop")
async def beep(message):
    await message.channel.send("Boop")

@client.command(description="Pings somone? Idk\n .mention <mention>")
async def mention(ctx, member : discord.Member):
    await ctx.send(f"{member.mention}")

@client.command(description="Pings flics for some good old wingman",hidden=True)
async def wm(ctx,num=6):
    if ctx.author.id==me:
        flicsMen=client.get_user(flics)
        for i in range(int(num)):
            await ctx.send(f"{flicsMen.mention} wm?")



@client.command(description="Pings someone a bunch of times\n .spam <mention> <number> <content>")
async def spam(ctx, member : discord.Member, num=10, *, words="words"):
    if member.id==me:
        num=5
    left=num
    #and notMe(member.id)
    if (ctx.author.id in AdMo.admin):
        for i in range(int(num)):
            await ctx.send(f"{member.mention}, {words}")
            time.sleep(.5)
            left-=1
            print(f'Sent: "{words}" to {member}, {left} remaining')

@client.command(description="Repeats a message\n .rep <number> <content>")
async def rep(ctx, num=10, *, words="words"):
    left=num
    if (ctx.author.id in AdMo.admin):
        for i in range(int(num)):
            await ctx.send(words)
            time.sleep(.5)
            left-=1
            print(f'Repeated: "{words}", {left} remaining')

@client.command(description="Dms someone a bunch of times\n .dm <mention> <number> <content>")
async def dm(ctx, member : discord.Member, num=10, *, words="words"):
    if member.id==me:
        num=5
    left=num
    if (ctx.author.id in AdMo.admin):
        for i in range(int(num)):
            await member.send(f"{member.mention}, {words}")
            time.sleep(.5)
            left-=1
            print(f'Sent: "{words}" to {member}, {left} remaining')

@client.command(description="Resets status loop",hidden=True)
async def status(ctx):
    if ctx.author.id==me:
        stat.cancel()
        stat.start()


@client.command(description="Clears some messages\n .clear <number>")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, num=6):
    await ctx.channel.purge(limit=num+1)

@client.command(description="Don't worry about it",hidden=True)
async def void(ctx, num=6):
    if (ctx.author.id in AdMo.admin):
        await ctx.channel.purge(limit=num+1)

@client.command(description="Adds/removes someone to admin list\n .admin <mention>")
async def admin(ctx, member : discord.Member):
    if ctx.author.id==me:
        func.adminMock(member.id,0)

@client.command(description="Adds/removes someone to mock list\n .mock <mention>")
async def mock(ctx, member : discord.Member):
    func.adminMock(member.id,1)

@client.command(description="Shows the AdMo list\n .admo <mention>")
async def admo(ctx):
    embed = make_embed(ctx, title='admo',description=(f"Admin: {AdMo.admin}\nMocking: {AdMo.mocking}"))
    await ctx.send(embed=embed)

@client.command(description="Send a picture to the bot's email\n .send <image link>")
async def send(ctx,link):
    sub=f"{ctx.author} sent you a picture!!"
    body="This picture was sent through your bot"
    attach=[link]
    botMail.send(sub,body,attach)
    await ctx.send("Image sent!")

@client.command(description="Grabs a random Wikipedia Article")
async def wiki(ctx):
    link=func.wikiRand()
    title=func.wikiTitle(link)
    await ctx.send(f"{title} \n{link}")

@client.command(description="Clears Gil Bot Messages\n .clean <number>")
async def clean(ctx, num=6):
    def is_me(m):
        return m.author == client.user
    deleted = await ctx.channel.purge(limit=num, check=is_me)
    msg = await ctx.channel.send('Deleted {} message(s)'.format(len(deleted)))
    await msg.delete(delay=2.5)

@client.command(description="Clears Member Messages\n .sift <mention>")
@commands.has_permissions(manage_messages=True)
async def sift(ctx, member : discord.Member, num=6):
    def is_them(m):
        return m.author == member
    deleted = await ctx.channel.purge(limit=num, check=is_them)
    msg = await ctx.channel.send('Deleted {} message(s)'.format(len(deleted)))
    await msg.delete(delay=2.5)

@client.command(description="Also don't worry about it\n .vsift <mention>",hidden=True)
async def vsift(ctx, member : discord.Member, num=6):
    if ctx.author.id in AdMo.admin:
        def is_them(m):
            return m.author == member
        deleted = await ctx.channel.purge(limit=num, check=is_them)
        msg = await ctx.channel.send('Deleted {} message(s)'.format(len(deleted)))
        await msg.delete(delay=2.5)

@client.command(description='Kick someone\n .kick <mention> <reason>',hidden=True)
async def kick(ctx, member: discord.Member, reason=None):
    if (ctx.author.id in AdMo.admin) and (member.id not in AdMo.admin):
        await member.kick(reason=reason)
        await ctx.send(f'{member} kicked because: {reason}')

##@client.command(description="Minion haha")
##async def bello(ctx):
##    await ctx.send(str(random.choice(lists.minion)))

spacer="        "

@client.command(description="Minion haha",aliases=["minion","bello"])
async def minyin(ctx):
    info=redditGrab.imageScrape("MinionMemes")
    if info[3]==True and ctx.channel.is_nsfw()==False:
        await ctx.send(embed=make_embed(ctx,title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
    else:
        await ctx.send(embed=make_embed(ctx,title=info[0],image=info[1],footer=f"Posted on r/{info[2]}{spacer}"+str(datetime.datetime.now()).split('.')[0]))

@client.command(description="Top Tier Sesame Street")
async def bert(ctx):
    info=redditGrab.imageScrape("bertstrips")
    if info[3]==True and ctx.channel.is_nsfw()==False:
        await ctx.send(embed=make_embed(ctx,title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
    else:
        await ctx.send(embed=make_embed(ctx,title=info[0],image=info[1],footer=f"Posted on r/{info[2]}{spacer}"+str(datetime.datetime.now()).split('.')[0]))

@client.command(description="MEEM", aliases=["mem","emem","meem","memes"])
async def meme(ctx):
    info=redditGrab.imageScrape("dankmemes")
    if info[3]==True and ctx.channel.is_nsfw()==False:
        await ctx.send(embed=make_embed(ctx,title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
    else:
        await ctx.send(embed=make_embed(ctx,title=info[0],image=info[1],footer=f"Posted on r/{info[2]}{spacer}"+str(datetime.datetime.now()).split('.')[0]))

@client.command(description="Gets only the finest images on the web")
async def blursed(ctx):
    info=redditGrab.imageScrape("blursedimages")
    if info[3]==True and ctx.channel.is_nsfw()==False:
        await ctx.send(embed=make_embed(ctx,title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
    else:
        await ctx.send(embed=make_embed(ctx,title=info[0],image=info[1],footer=f"Posted on r/{info[2]}{spacer}"+str(datetime.datetime.now()).split('.')[0]))

@client.command(description="Gets some copypasta",aliases=["pasta"])
async def copypasta(ctx):
    info=redditGrab.textScrape("copypasta")
    if info[3]==True and ctx.channel.is_nsfw()==False:
        await ctx.send(embed=make_embed(ctx,title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
    else:
        await ctx.send(embed=make_embed(ctx,title=info[0],description=info[1],footer=f"Posted on r/{info[2]}{spacer}"+str(datetime.datetime.now()).split('.')[0]))

@client.command(description="Gets a post off any sub\n .reddit <sub name>")
async def reddit(ctx, sub):
    info=redditGrab.imageScrape(sub)
    if info[3]==True and ctx.channel.is_nsfw()==False:
        await ctx.send(embed=make_embed(ctx,title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
    else:
        await ctx.send(embed=make_embed(ctx,title=info[0],image=info[1],footer=f"Posted on r/{info[2]}{spacer}"+str(datetime.datetime.now()).split('.')[0]))

@client.command(description="Gets a Text-post off any sub\n .textpost <sub name>",aliases=["textP","text"])
async def textpost(ctx, sub):
    info=redditGrab.textScrape(sub)
    if info[3]==True and ctx.channel.is_nsfw()==False:
        await ctx.send(embed=make_embed(ctx,title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
    else:
        await ctx.send(embed=make_embed(ctx,title=info[0],description=info[1],footer=f"Posted on r/{info[2]}{spacer}"+str(datetime.datetime.now()).split('.')[0]))

@client.command(description="Gets posts from a user\n .redditor <username>")
async def redditor(ctx, user):
    info=redditGrab.userImageScrape(user)
    if info[3]==True and ctx.channel.is_nsfw()==False:
        await ctx.send(embed=make_embed(ctx,title="Sorry, I can't send this post to a non-NSFW channel",footer="Try using the command again or make the channel NSFW"))
    else:
        await ctx.send(embed=make_embed(ctx,title=info[0],image=info[1],footer=f"Posted on r/{info[2]}{spacer}"+str(datetime.datetime.now()).split('.')[0]))

@client.command(description="Fetches a users karma\n .karma <username>")
async def karma(ctx, user):
    num=redditGrab.karmaScrape(user)
    await ctx.send(f"{user.capitalize()} has {num} karma")

@client.command(description="Check the number of times someone's said a word\n .fetch <mention>")
async def fetch(ctx, member : discord.Member,word):
    wordNum=func.wordGrab(str(member.id),word)
    await ctx.send(f"{member.mention} has said {word} {wordNum} times.")

@client.command(description="Shows the tracked words")
async def tracked(ctx):
    embed = make_embed(ctx, title='Tracked Words',description=f"{counted}")
    await ctx.send(embed=embed)

@client.command(description="Yes hahaha very funny meem\n .sponge <content>")
async def sponge(ctx, *, words):
  await ctx.send(func.sponge(words))

@client.command(description="Send the invite link")
async def invite(ctx):
    embed=make_embed(ctx,title="Invite me to your server!",link="https://discord.com/api/oauth2/authorize?client_id=702143271144783904&permissions=8&scope=bot")
    await ctx.send(embed=embed)


@client.command(description="Die",aliases=["kill"])
async def reload(ctx):
    if ctx.author.id==me:
        await ctx.send(f"{random.choice(lists.die)}")
        quit()


##@client.command(description="Die",aliases=["kill"])
##async def die(ctx):
##    if str(ctx.author.id)==me:
##        await ctx.send(str(random.choice(lists.die)))
##        quit()


client.run('NzAyMTQzMjcxMTQ0NzgzOTA0.Xp7v4Q.p-XDpxrKKsz7YL6Ry7gQdKO0IAg')
