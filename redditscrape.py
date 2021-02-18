
import praw
import pandas as pd

'''
Create Reddit app on their Website
it will provide a the info like client_id, client_secret, user_agent
'''
client_id = <client_id>
client_secret = <client_secret>
user_agent = <user_agent>
limit = 100
topic_you_want_scrap_on = 'MachineLearning'

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

posts = []
ml_subreddit = reddit.subreddit(topic_you_want_scrap_on)
for post in ml_subreddit.hot(limit=limit):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
