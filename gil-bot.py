import discord
from discord.ext import commands
import random
import redditGrab
import time
import datetime
##import sys
import lists
import func


#Me, Connor, Mark, Flics
admin=["382987612736192512","640393413425889314","694254356601503855","264808033220165632"]
#Millie, Toby
mocking=["487403997393715210","265581590086680576"]

me="382987612736192512"
botID="702143271144783904"

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('{0.user}'.format(client)+" is online")
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
    if any(ele in (message.content.lower()) for ele in lists.swears):
        if str(message.author.id)!= "702143271144783904":
            if random.randint(0,100)==69:
                await message.channel.send("Woah there. Watch your language.")
    if "fuck" in message.content.lower():
        if str(message.author.id)!="702143271144783904":
            num=func.phraseNum(message.content.lower(),"fuck")
            func.fuckAdd(message.author.id,num)
            print("Added "+str(num)+" to "+str(message.author)+"'s fuck count")
    if "ilan" in message.content.lower():
        if str(message.author.id)!= "702143271144783904":
            await message.channel.send(str(("Guys remember that time "+random.choice(lists.ilan))))
    if "delyeet" in message.content.lower():
        if str(message.author.id)!= "702143271144783904":
            await message.delete()
    if str(message.author.id)==("462885213215916034"):
        await message.channel.send('Shut up Frog.')
        await message.delete()
    if str(message.author.id) in mocking:
        await message.channel.send(func.sponge(message.content))
    else:
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
    if (str(ctx.author.id) in admin) and (str(member.id)!=me):
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
    if (str(ctx.author.id) in admin):
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
    if (str(ctx.author.id) in admin) and (str(member.id)!=me):
        for i in range(int(num)):
            await member.send(f"{member.mention}, "+str(words))
            time.sleep(.5)
            left-=1
            print("Sent: \""+str(words)+"\" to "+str(member)+" "+str(left)+" remaining")
    else:
        pass

@client.command(description="Clears some messages\n .clear <number>")
@commands.has_permissions(ban_members=True, kick_members=True)
async def clear(ctx, num=6):
    await ctx.channel.purge(limit=num+1)

@client.command(description="Clears some messages")
async def void(ctx, num=6):
    if (str(ctx.author.id) in admin):
        await ctx.channel.purge(limit=num+1)

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

@client.command(description='Kick someone\n .kick <mention> <reason>')
async def kick(ctx, member: discord.Member, reason=None):
    if (str(ctx.author.id) in admin) and (str(member.id) not in admin):
        await member.kick(reason=reason)
        await ctx.send(f'{member} kicked because: {reason}')

##@client.command(description="Minion haha")
##async def bello(ctx):
##    await ctx.send(str(random.choice(lists.minion)))

@client.command(description="Minion haha")
async def minyin(ctx):
    info=redditGrab.imageScrape("MinionMemes")
    await ctx.send(info[0])
    await ctx.send(info[1])

@client.command(description="Top Tier Sesame Street")
async def bert(ctx):
    info=redditGrab.imageScrape("bertstrips")
    await ctx.send(info[0])
    await ctx.send(info[1])

@client.command(description="MEEM", aliases=["mem","emem","meem"])
async def meme(ctx):
    info=redditGrab.imageScrape("dankmemes")
    await ctx.send(info[0])
    await ctx.send(info[1])

@client.command(description="Blursed Images")
async def blursed(ctx):
    info=redditGrab.imageScrape("blursedimages")
    await ctx.send(info[0])
    await ctx.send(info[1])

@client.command(description=".reddit <sub name>")
async def reddit(ctx, sub):
    info=redditGrab.imageScrape(sub)
    await ctx.send(info[0])
    await ctx.send(info[1])

@client.command(description="Check the number of times someone's said fuck\n .frick <mention>")
async def frick(ctx, member : discord.Member):
    fuckNum=func.fuckGrab(member.id)
    await ctx.send(f"{member.mention}"+" has said the frick word "+str(fuckNum)+" times.")

@client.command(description="Yes hahaha very funny meem\n .sponge <content>")
async def sponge(ctx, *, words):
  await ctx.send(func.sponge(words))

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


client.run('NzAyMTQzMjcxMTQ0NzgzOTA0.Xp7wew.lqrG8WSK2aAUlMam43UfMxgcl94')
