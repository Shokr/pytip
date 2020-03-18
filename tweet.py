import csv
import re

import tweepy

auth = tweepy.OAuthHandler('P4L0JIFEH8abGpiDCJZZfNwxJ', 'HGJS3zbqH57S5Blqpm6wOe4sUoZnaBOpeKttrcb9FTUu8jGU0H')
auth.set_access_token('2716340250-mbZpFIuiz2uGWMm7sjbcM1XOz70abbT2RbVhWNb',
                      'Ey5yzvxNKxBtBN1itIhDJMBMkMJxG2wNFNe0iKVNFmGzd')

api = tweepy.API(auth)

name = "python_tip"
tweetCount = 20
results = api.user_timeline(id=name, count=tweetCount)

with open('tweets.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        ['IdTweet', 'TweetText', 'TimeCreated', 'RetweetCount', 'FavoriteCount', 'Urls', 'medias', 'hashtags'])
    for tweet in results:
        urls = tweet.entities['urls']
        hashtags = tweet.entities['hashtags']
        if 'media' in tweet.entities:
            medias = tweet.entities['media']
        else:
            medias = ''
        # text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', tweet.text, flags=re.MULTILINE)
        text = re.sub(r'&gt;', '>', tweet.text, flags=re.MULTILINE)
        writer.writerow(
            [tweet.id, text, tweet.created_at, tweet.retweet_count, tweet.favorite_count, urls, medias, hashtags])
