import csv
import re

import tweepy

# from celery.schedules import crontab
# from celery.task import periodic_task


auth = tweepy.OAuthHandler('P4L0JIFEH8abGpiDCJZZfNwxJ', 'HGJS3zbqH57S5Blqpm6wOe4sUoZnaBOpeKttrcb9FTUu8jGU0H')
auth.set_access_token('2716340250-mbZpFIuiz2uGWMm7sjbcM1XOz70abbT2RbVhWNb',
                      'Ey5yzvxNKxBtBN1itIhDJMBMkMJxG2wNFNe0iKVNFmGzd')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# The Twitter user who we want to get tweets from
name = "python_tip"
# Number of tweets to pull
tweetCount = 10

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

########################################################################################################################
# @periodic_task(run_every=(crontab(minute='360')), name="sync_tweets",)
########################################################################################################################
with open('tweets.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['IdTweet', 'TweetText', 'TimeCreated', 'RetweetCount', 'FavoriteCount'])
    for tweet in results:
        # text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', tweet.text, flags=re.MULTILINE)
        text = re.sub(r'&gt;', '>', tweet.text, flags=re.MULTILINE)
        writer.writerow([tweet.id, text, tweet.created_at, tweet.retweet_count, tweet.favorite_count])

########################################################################################################################

with open('urls.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['IdTweet', 'URL'])
    for tweet in results:
        urls = tweet.entities['urls']
        for url in urls:
            writer.writerow([tweet.id, url['expanded_url']])

########################################################################################################################

with open('images.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['IdTweet', 'Image'])
    for tweet in results:
        if 'media' in tweet.entities:
            urls = tweet.entities['media']
            for url in urls:
                writer.writerow([tweet.id, url['media_url']])

########################################################################################################################

with open('hashtags.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['IdTweet', 'Tag'])
    for tweet in results:
        hashtags = tweet.entities['hashtags']
        for tag in hashtags:
            writer.writerow([tweet.id, tag['text']])
