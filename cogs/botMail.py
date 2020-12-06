import imghdr
import smtplib
import urllib.request
from email.message import EmailMessage

import discord
from discord.ext import commands, tasks
from func import listToString, mailSend
from gil_bot import PREFIX

#To add:
##Sending Emails and shit, guild and post if need be

class BotMail(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.bot='gildiscordbot@gmail.com'
    self.EMAIL_PASSWORD = 'qppcxazktetownat'

  # def mailSend(self, fromAddress, toAddress, subject, body, attachment=None):
  #   msg = EmailMessage()
  #   msg['Subject'] = subject
  #   msg['From'] = fromAddress
  #   msg['To'] = toAddress
  #   msg.set_content(body)
  #   if attachment:
  #       for i in attachment:
  #           urllib.request.urlretrieve(i, "sample.png")
  #           with open("sample.png", 'rb') as fp:
  #               img_data = fp.read()
  #           msg.add_attachment(img_data, maintype='image',
  #                           subtype=imghdr.what(None, img_data))   
  #   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  #       smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
  #       smtp.send_message(msg)


  @commands.command(description=f"Send a picture to the bot's email\n {PREFIX}send <image link>")
  async def send(self, ctx, link):
    sub=f"{ctx.author} sent you a picture!!"
    body="This picture was sent through your bot"
    attach=[link]
    mailSend(sub, body, attachment=attach)
    await ctx.send("Image sent!", delete_after=2.5)
    #await msg.delete(delay=2.5)
  
  @commands.command(description=f"Saves messages for posterity\n {PREFIX}post <number>",hidden=True)
  async def post(self, ctx, num=20):
    mList=[]
    async for message in ctx.channel.history(limit=num):
        mList.insert(0,f"{message.author}: {message.content}\n")
    sub=f"Posterity request from {ctx.channel} on {ctx.guild}"
    body=listToString(mList)
    mailSend(sub, body)
    await ctx.send("Sent!", delete_after=2.5)


def setup(client):
  client.add_cog(BotMail(client))

