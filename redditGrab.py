import praw

reddit = praw.Reddit(client_id="wqA7c3mg7FNPXQ",
                     client_secret="Iy2LJpk8ggekoZZaag-iBXgEnnw",
                     user_agent="android:com.example.myredditapp:v1.2.3 (by u/Giruchan)")

#print(reddit.read_only)

def imageScrape(sub):
    import random
    temp={}
    posts=reddit.subreddit(sub).hot()
    post_to_pick=random.randint(1, 75)
    for i in range(post_to_pick):
        submission = next(x for x in posts if not x.stickied)
        if (".jpg" in submission.url) or (".png" in submission.url) or (".gif" in submission.url):
            temp[submission.url]=(submission.title,submission.subreddit,submission.over_18)
    pickedUrl=random.choice(list(temp.keys()))
    pickedData=temp[pickedUrl]
    pickedInfo=(pickedData[0],pickedUrl,pickedData[1],pickedData[2])
    return pickedInfo

def karmaScrape(user):
    redditor=reddit.redditor(user)
    return redditor.link_karma + redditor.comment_karma

def userImageScrape(user):
    import random
    temp={}
    #posts=reddit.redditor(user).submissions.top("all")
    #post_to_pick=random.randint(1, 75)
    #count=post_to_pick
    for submission in reddit.redditor(user).submissions.top("all"):
        if (".jpg" in submission.url) or (".png" in submission.url) or (".gif" in submission.url):
            temp[submission.url]=(submission.title,submission.subreddit)
    pickedUrl=random.choice(list(temp.keys()))
    pickedData=temp[pickedUrl]
    pickedInfo=(pickedData[0],pickedUrl,pickedData[1])
    return pickedInfo

def textScrape(sub):
    import random
    temp={}
    posts=reddit.subreddit(sub).hot()
    post_to_pick=random.randint(1, 75)
    for i in range(post_to_pick):
        submission = next(x for x in posts if not x.stickied)
        #if (".jpg" in submission.url) or (".png" in submission.url) or (".gif" in submission.url):
        temp[submission.selftext]=(submission.title,submission.subreddit,submission.over_18)
    pickedUrl=random.choice(list(temp.keys()))
    pickedData=temp[pickedUrl]
    pickedInfo=(pickedData[0],pickedUrl,pickedData[1],pickedData[2])
    return pickedInfo
