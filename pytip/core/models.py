from django.db import models
from django.utils import timezone


class Tweet(models.Model):
    tweet = models.FloatField(db_column='IdTweet', primary_key=True)
    text = models.TextField(db_column='TweetText', blank=True, null=True)
    created_at = models.DateTimeField(db_column='TimeCreated', default=timezone.now)
    retweet_count = models.BigIntegerField(db_column='RetweetCount', blank=True, null=True)
    favorite_count = models.BigIntegerField(db_column='FavoriteCount', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tweets'

        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

        ordering = ['-created_at']

    def __str__(self):
        return '[{}] - {}'.format(self.tweet, self.text)


class Url(models.Model):
    tweet = models.ForeignKey(to='Tweet', on_delete=models.CASCADE, db_column='IdTweet')
    url = models.URLField(db_column='URL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urls'

        verbose_name = 'Url'
        verbose_name_plural = 'Urls'

    def __str__(self):
        return '{}'.format(self.url)


class Image(models.Model):
    tweet = models.ForeignKey(to='Tweet', on_delete=models.CASCADE, db_column='IdTweet')
    image = models.URLField(db_column='Image', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'

        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return '{}'.format(self.image)


class Hashtag(models.Model):
    tweet = models.ForeignKey(to='Tweet', on_delete=models.CASCADE, db_column='IdTweet')
    tag = models.TextField(db_column='Tag', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hashtags'

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return '{}'.format(self.tag)
