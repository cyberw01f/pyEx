#!pypy/bin/python
import praw
reddit = praw.Reddit('rPyBot')
subreddit=reddit.subreddit("jokes")
for submission in subreddit.new(limit=1):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
