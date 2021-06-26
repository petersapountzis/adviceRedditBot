import praw
import random
import time
import json


reddit = praw.Reddit(client_id='1rhONTIvB-YZ5w',
                     client_secret='zr6tLc3bK7XWTOvt93uev0NyI_1ccw',
                     user_agent='<console:TEST:1.0>',
                     username='petuporu',
                     password='mary0923')

subreddit = reddit.subreddit("ApplyingToCollege")

sad_quotes = ["Sadness flies away on the wings of time. - Ean de La Fontaine",
              "The walls we build around us to keep sadness out also keeps out the joy. - Jim Rohn",
              "In deep sadness there is no place for sentimentality. - William S. Burroughs",
              "Sadness is but a wall between two gardens. -Kahlil Gibran"]


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
               random_index = random.randint(0,len(sad_quotes) - 1) 
               comment.reply(sad_quotes[random_index])
               