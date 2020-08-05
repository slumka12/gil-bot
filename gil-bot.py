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

me="382987612736192512"
botID="702143271144783904"

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
    if str(message.author) == 'Connor Bot#9505':
        return await message.channel.send("Hello fellow bot")
    if "turtle" in message.content.lower():
        if str(message.author.id)!= "702143271144783904":
            await message.channel.send("We don't say that name in this house")
    if ("superhot" in message.content.lower())or("super hot" in message.content.lower()):
        if str(message.author.id)!= "702143271144783904":
            for i in range(4):
                await message.channel.send("SUPER")
                time.sleep(.5)
                await message.channel.send("HOT")
                time.sleep(.75)
    if any(ele in (message.content.lower()) for ele in lists.swears):
        if str(message.author.id)!= "702143271144783904":
            if random.randint(0,100)==69:
                await message.channel.send("Woah there. Watch your language.")
    if any(word in message.content.lower() for word in counted):
        if str(message.author.id)!="702143271144783904":
            for i in counted:
                if i in message.content.lower():
                    num=func.phraseNum(message.content.lower(),i)
                    func.wordAdd(str(message.author.id),i,num)
    if "ilan" in message.content.lower():
        if str(message.author.id)!= "702143271144783904":
            await message.channel.send(str(("Guys remember that time "+random.choice(lists.ilan))))
    if "delyeet" in message.content.lower():
        if str(message.author.id)!= "702143271144783904":
            await message.delete()
    if str(message.author.id)==("462885213215916034"):
        await message.channel.send('Shut up Frog.')
        await message.delete()
    if str(message.author.id) in AdMo.mocking:
        await message.channel.send(func.sponge(message.content))
    if True==True:
        await client.process_commands(message)

#####Commands
        
client.remove_command("help")

@client.command(pass_context=True)
async def help(ctx, com=None):
    if not com:
        listcom = list(client.commands)
        commands = ''
        for command in listcom:
            commands+=f'.{command}\n'
        embed = make_embed(ctx,
            title='Commands',
            description=commands+''
        )
        await ctx.send(embed=embed)
    elif com != 'help':
        try:
            comm = client.get_command(com)
            embed = make_embed(ctx,
                title='.'+com,
                description=comm.description,
                footer=str(datetime.datetime.now()).split('.')[0]
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

@client.command(description="Pings someone a bunch of times\n .spam <mention> <number> <content>")
async def spam(ctx, member : discord.Member, num=10, *, words):
    left=num
    if (str(ctx.author.id) in AdMo.admin) and (str(member.id)!=me):
        for i in range(int(num)):
            await ctx.send(f"{member.mention}, "+str(words))
            time.sleep(.5)
            left-=1
            print("Sent: \""+str(words)+"\" to "+str(member)+" "+str(left)+" remaining")
    else:
        pass

@client.command(description="Repeats a message\n .rep <number> <content>")
async def rep(ctx, num=10, *, words):
    left=num
    if (str(ctx.author.id) in AdMo.admin):
        for i in range(int(num)):
            await ctx.send(str(words))
            time.sleep(.5)
            left-=1
            print("Repeated:\""+str(words)+"\" "+str(left)+" remaining")
    else:
        pass

@client.command(description="Dms someone a bunch of times\n .dm <mention> <number> <content>")
async def dm(ctx, member : discord.Member, num=10, *, words):
    left=num
    if (str(ctx.author.id) in AdMo.admin) and (str(member.id)!=me):
        for i in range(int(num)):
            await member.send(f"{member.mention}, "+str(words))
            time.sleep(.5)
            left-=1
            print("Sent: \""+str(words)+"\" to "+str(member)+" "+str(left)+" remaining")
    else:
        pass

@client.command(description="Clears some messages\n .clear <number>")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, num=6):
    await ctx.channel.purge(limit=num+1)

@client.command(description="Clears some messages")
async def void(ctx, num=6):
    if (str(ctx.author.id) in AdMo.admin):
        await ctx.channel.purge(limit=num+1)

@client.command(description="Adds/removes someone to admin list\n .admin <mention>")
async def admin(ctx, member : discord.Member):
    if str(ctx.author.id)==me:
        func.adminMock(str(member.id),0)

@client.command(description="Adds/removes someone to mock list\n .mock <mention>")
async def mock(ctx, member : discord.Member):
    func.adminMock(str(member.id),1)

@client.command(description="Shows the AdMo list\n .admo <mention>")
async def admo(ctx):
    embed = make_embed(ctx, title='admo',description=("Admin: "+str(AdMo.admin)+"\nMocking: "+str(AdMo.mocking)))
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
    await ctx.send(str(title)+"\n"+str(link))

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

@client.command(description="Clears Member Messages\n .vsift <mention>")
async def vsift(ctx, member : discord.Member, num=6):
    if str(ctx.author.id) in AdMo.admin:
        def is_them(m):
            return m.author == member
        deleted = await ctx.channel.purge(limit=num, check=is_them)
        msg = await ctx.channel.send('Deleted {} message(s)'.format(len(deleted)))
        await msg.delete(delay=2.5)

@client.command(description='Kick someone\n .kick <mention> <reason>')
async def kick(ctx, member: discord.Member, reason=None):
    if (str(ctx.author.id) in AdMo.admin) and (str(member.id) not in AdMo.admin):
        await member.kick(reason=reason)
        await ctx.send(f'{member} kicked because: {reason}')

##@client.command(description="Minion haha")
##async def bello(ctx):
##    await ctx.send(str(random.choice(lists.minion)))

@client.command(description="Minion haha",aliases=["minion","bello"])
async def minyin(ctx):
    info=redditGrab.imageScrape("MinionMemes")
    await ctx.send(info[0]+"\n"+info[1])

@client.command(description="Top Tier Sesame Street")
async def bert(ctx):
    info=redditGrab.imageScrape("bertstrips")
    await ctx.send(info[0]+"\n"+info[1])

@client.command(description="MEEM", aliases=["mem","emem","meem"])
async def meme(ctx):
    info=redditGrab.imageScrape("dankmemes")
    await ctx.send(info[0]+"\n"+info[1])

@client.command(description="Gets only the finest images on the web")
async def blursed(ctx):
    info=redditGrab.imageScrape("blursedimages")
    await ctx.send(info[0]+"\n"+info[1])

@client.command(description="Gets a post off any sub\n .reddit <sub name>")
async def reddit(ctx, sub):
    info=redditGrab.imageScrape(sub)
    await ctx.send(info[0]+"\n"+info[1])

@client.command(description="Gets posts from a user\n .redditor <username>")
async def redditor(ctx, user):
    info=redditGrab.userImageScrape(user)
    await ctx.send(info[0]+"\n"+info[1])

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
    embed = make_embed(ctx, title='Tracked Words',description=(str(counted)))
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
    if str(ctx.author.id)==me:
        await ctx.send(str(random.choice(lists.die)))
        quit()


##@client.command(description="Die",aliases=["kill"])
##async def die(ctx):
##    if str(ctx.author.id)==me:
##        await ctx.send(str(random.choice(lists.die)))
##        quit()


client.run('NzAyMTQzMjcxMTQ0NzgzOTA0.Xp7v4Q.p-XDpxrKKsz7YL6Ry7gQdKO0IAg')
