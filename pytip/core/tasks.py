import re
from time import sleep

import tweepy
from celery.schedules import crontab
from celery.task import periodic_task

from pytip.core.models import Tweet


@periodic_task(run_every=(crontab(minute='*/15')), name="sync_tweets", ignore_result=True)
def sync_tweets():
    auth = tweepy.OAuthHandler('P4L0JIFEH8abGpiDCJZZfNwxJ', 'HGJS3zbqH57S5Blqpm6wOe4sUoZnaBOpeKttrcb9FTUu8jGU0H')
    auth.set_access_token('2716340250-mbZpFIuiz2uGWMm7sjbcM1XOz70abbT2RbVhWNb',
                          'Ey5yzvxNKxBtBN1itIhDJMBMkMJxG2wNFNe0iKVNFmGzd')

    api = tweepy.API(auth)

    results = api.user_timeline(id="python_tip", count=10)

    for tweet in results:

        if Tweet.objects.filter(tweet=tweet.id).exists() is True:
            print('Updating..')
            print(tweet.id)

            Tweet.objects.filter(tweet=tweet.id).update(re_tweet_count=tweet.retweet_count,
                                                        favorite_count=tweet.favorite_count)
        else:

            urls = tweet.entities['urls']
            hashtags = tweet.entities['hashtags']

            if 'media' in tweet.entities:
                medias = tweet.entities['media']
            else:
                medias = ''

            text = re.sub(r'&gt;', '>', tweet.text, flags=re.MULTILINE)

            print('Insert..')
            print(tweet.id)

            tweet = Tweet.objects.create(tweet=tweet.id, text=text, created_at=tweet.created_at,
                                         re_tweet_count=tweet.retweet_count, favorite_count=tweet.favorite_count,
                                         urls=urls, medias=medias, tags=hashtags)
            tweet.save()

            sleep(5)


sync_tweets()
