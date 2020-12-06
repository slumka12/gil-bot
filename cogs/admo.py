import json

import discord
from discord.ext import commands, tasks
from func import listToString, make_embed, memlistToString, userGrab
from gil_bot import PREFIX, me


class AdMo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(description=f"Edits or Shows Admin List\n {PREFIX}Admin <user>")
    async def admin(self, ctx, user : discord.Member = None):
        action = None
        with open ("admo.json","r") as j:
            mJson = json.load(j)
        #print(f"before: {mJson}")
        if user and ctx.author.id == me:
            if user.id in mJson["admin"]:
                mJson["admin"].remove(user.id)
                action = f"{userGrab(self.client, users = [user.id])[0].name} removed successfully!"
            else:
                mJson["admin"].append(user.id)
            #print(f"after {mJson}")
                action = f"{userGrab(self.client, users = [user.id])[0].name} added successfully!"
            with open("admo.json","w") as j:
                json.dump(mJson, j, indent=2, sort_keys=True)
        await ctx.send(embed=make_embed(title="Admin List",
        description=f'{memlistToString(self.client, mJson["admin"], separator=", ")}', footer=action))

def setup(client):
  client.add_cog(AdMo(client))





# def adminMock(self,userId, mode):
#     import AdMo
#     listA=AdMo.admin
#     listM=AdMo.mocking
#     listS=AdMo.silence
#     if mode==0:
#         if userId in listA:
#             listA.remove(userId)
#         elif userId not in listA:
#             listA.append(userId)
#     elif mode==1:
#         if userId in listM:
#             listM.remove(userId)
#         elif userId not in listM:
#             listM.append(userId)
#     elif mode==2:
#         if userId in listS:
#             listS.remove(userId)
#         elif userId not in listS:
#             listS.append(userId)
    
#     file=open("AdMo.py","w")
#     file.write("admin="+str(listA)+"\nmocking="+str(listM)+"\nsilence="+str(listS))
#     file.close()



# admin=[382987612736192512, 640393413425889314, 264808033220165632]
# mocking=[]
# silence=[]
