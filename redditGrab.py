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
            temp[submission.url]=submission.title
    pickedUrl=random.choice(list(temp.keys()))
    #print(pickedUrl)
    pickedTitle=temp[pickedUrl]
    #print(pickedTitle)
    pickedInfo=(pickedTitle,pickedUrl)
    return pickedInfo
