import praw
import random
import time
import json

#Use your own client ID, secret ID, etc. Go to https://www.reddit.com/prefs/apps/ to make your own. 
reddit = praw.Reddit(client_id='<clientKey>',
                     client_secret='<secretID>',
                     user_agent='<userAgent>',
                     username='<username>',
                     password='<password>')

subreddit = reddit.subreddit("ApplyingToCollege")

advice = ["Go touch some grass",
              "Get some fresh air and reevaluate",
              "I'm sure it'll all work out",
              "Hang in there!"]


#lists front page posts
#for submission in reddit.front.hot():
    #print(submission)

for submission in subreddit.hot(limit=5):
    #print("***************")
   # print(submission.title)

   
    #commenting one of the four sad quotes when it sees the word "safety" in a comment
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if " stressed " in comment_lower:
               print ("------------------------------------------")
               print (comment.body)
               random_index = random.randint(0,len(advice) - 1) 
               comment.reply(advice[random_index])
               
