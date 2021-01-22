#All the functions for the bot
import datetime
import imghdr
import json
import random
import smtplib
import urllib.request
from email.message import EmailMessage

import discord
from discord.ext import commands, tasks

bot='gildiscordbot@gmail.com'
EMAIL_PASSWORD = 'qppcxazktetownat'
#Imports: imghdr, smtplib, urllib.request, from email.message import EmailMessage
def mailSend(subject, body, fromAddress=bot, toAddress=bot, attachment=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg.set_content(body)
    if attachment!=None:
        for i in attachment:
            urllib.request.urlretrieve(i, "sample.png")
            with open("sample.png", 'rb') as fp:
                img_data = fp.read()
            msg.add_attachment(img_data, maintype='image',
                            subtype=imghdr.what(None, img_data))   
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(fromAddress, EMAIL_PASSWORD)
        smtp.send_message(msg)

def tget():
    with open("t.txt","r") as f:
        return f.readline()

def jsGet(fName):
    with open (f"{fName}.json","r") as j:
        return json.load(j)

# def make_embed(title=None, description=None, color=None, author=None, image=None, link=None, footer=None):
#     if not color: color = random.randint(0, 0xffffff)
#     embed = discord.Embed(
#         title=title,
#         url=link,
#         description=description,
#         color=color
#     )
#     if author: embed.set_author(name=author)
#     if image: embed.set_image(url=image)
#     if footer: embed.set_footer(text=footer)
#     else: embed.set_footer(text=str(datetime.datetime.now()).split('.')[0])
#     return embed

def make_embed(title=None, description=None, color=None, author=None,
               image=None, link=None, footer=None, fields=None):
    if not color: color = discord.Color.random()
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
    if fields:
        for i in fields:
            embed.add_field(name = i[0], value=i[1],inline=i[2])
    return embed


def listToString(l:list, separator : str = "", endSep=None):
    s=""
    for i in l:
        if (l.index(i)==len(l)-2 and endSep!=None): separator = endSep
        #print(separator)
        s+=f"{i}{separator}"
    if separator != "": return s[:-len(separator)]
    else: return s

def stringToList(string : str, separator : str = " "):
    return [i for i in list(string.split(separator)) if i]

def removeChar(string, removes = []):
    for i in removes:
        string = string.replace(i, "")
    return string

def userGrab(client, users=[]):
    return [client.get_user(int(i)) for i in users]

def memlistToString(client, l:list, separator : str = ""):
    s = []
    for i in l:
        user = client.get_user(i)
        s.append(user.mention)
    return listToString(s,separator=separator)

def make_soup(url,feat="html"):
    import requests
    from bs4 import BeautifulSoup 
    data=requests.get(url).text
    return BeautifulSoup(data, features=feat)

def bible(link="https://dailyverses.net/random-bible-verse"):
    soup=make_soup(link, feat="html.parser")
    return (soup.find("a",attrs={"class":"vc"}).text,soup.find("span").text)

# def wikiRand():
#     soup=make_soup("https://en.wikipedia.org/wiki/Special:Random",feat="html.parser")
#     li=soup.find("li", attrs={"id":"ca-view"})
#     return f"https://en.wikipedia.org{li.find('a').attrs['href']}"

# def wikiTitle(link):
#     soup=make_soup(link,feat="html.parser")
#     h1=soup.find("h1")
#     return h1.text

def sponge(words):
    words=str(words)
    count=0
    final=""
    for i in words:
        if count==0:
            i=i.lower()
            count=1
        elif count==1:
            i=i.upper()
            count=0
        final=final+i
    return final


