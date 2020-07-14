#All the functions for the bot


def make_soup(url,feat="html"):
    import requests
    from bs4 import BeautifulSoup 
    data=requests.get(url).text
    soup=BeautifulSoup(data, features=feat)
    return soup

def wikiRand():
    soup=make_soup("https://en.wikipedia.org/wiki/Special:Random",feat="html.parser")
    li=soup.find("li", attrs={"id":"ca-view"})
    l=li.find("a").attrs["href"]
    return "https://en.wikipedia.org/"+l

def wikiTitle(link):
    soup=make_soup(link,feat="html.parser")
    h1=soup.find("h1")
    h=h1.text
    return h

def adminMock(userId, mode):
    import AdMo
    listA=AdMo.admin
    listM=AdMo.mocking
    if (userId in listA) and (mode==0):
        listA.remove(userId)
    elif (userId not in listA) and (mode==0):
        listA.append(userId)
    elif (userId in listM) and (mode==1):
        listM.remove(userId)
    elif (userId not in listM) and (mode==1):
        listM.append(userId)
    file=open("AdMo.py","w")
    file.write("admin="+str(listA)+"\nmocking="+str(listM))
    file.close()

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

def phraseNum(whole,part):
    if "`" not in whole:
        repChar="`"
    elif "~" not in whole:
        repChar="~"
    elif "|" not in whole:
        repChar="|"
    rep=whole.replace(part,repChar)
    count=0
    for i in rep:
        if i==repChar:
           count+=1
    return count

def wordAdd(memID,word,num):
    import json
    dumb=False
    file=open("wordCount.json","r")
    count=json.load(file)
    file.close()
    if memID not in count:
        temp=count["blank"]
        #print(temp)
        count.update({memID:temp})
        dumb=True
    elif memID in count:
        mem=count[memID]
        mem[word]+=num

    file=open("wordCount.json","w")
    json.dump(count,file)
    file.close()
    if dumb==True:
        interMed(memID, word, num)

def interMed(memID, word, num):
    wordAdd(memID, word, num)

def wordGrab(memID,word):
    import json
    file=open("wordCount.json","r")
    count=json.load(file)
    file.close()
    #print(count)
    if memID in count:
        mem=count[memID]
        return mem[word]
    if memID not in count:
        return "no"   



def keyAdd(key):
    import json
    file=open("wordCount.json","r")
    count=json.load(file)
    file.close()
    for i in count:
        mem=count[i]
        temp={key:0}
        mem.update(temp)
        print(mem)
    file=open("wordCount.json","w")
    json.dump(count,file)
    file.close()



##def fuckAdd(memID,num):
##    import ftime
##    fdic=ftime.dic
##    if memID in fdic:
##        fdic[memID]+=num
##    if memID not in fdic:
##        temp={memID:1}
##        fdic.update(temp)
##    file=open("ftime.py","w")
##    file.write("dic="+str(fdic))
##    file.close()
##def fuckGrab(memID):
##    import ftime
##    fdic=ftime.dic
##    if memID in fdic:
##        return fdic[memID]
##    if memID not in fdic:
##        return "no"

