from django.db import models
from django.utils import timezone

from pytip.users.models import User


class Tweet(models.Model):
    tweet = models.FloatField(db_column='IdTweet', unique=True)
    text = models.TextField(db_column='TweetText', max_length=280)
    created_at = models.DateTimeField(db_column='TimeCreated', default=timezone.now)
    re_tweet_count = models.BigIntegerField(db_column='RetweetCount', blank=True, null=True)
    favorite_count = models.BigIntegerField(db_column='FavoriteCount', blank=True, null=True)

    urls = models.TextField(db_column='Urls', blank=True, null=True)
    medias = models.TextField(db_column='Medias', blank=True, null=True)
    tags = models.TextField(db_column='Tags', blank=True, null=True)

    publisher = models.ForeignKey(to=User, related_name='PublisherUser',
                                  on_delete=models.CASCADE, db_column='IdPublisher', blank=True, null=True)
    published = models.BooleanField(db_column='Published', default=False)

    time_published = models.DateTimeField(db_column='TimePublished', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tweets'

        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

        ordering = ['-created_at']

    def __str__(self):
        return '[{}]'.format(self.tweet)
