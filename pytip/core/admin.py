from django.contrib import admin

from .froms import TweetForm
from .models import *


class TweetAdmin(admin.ModelAdmin):
    form = TweetForm

    search_fields = ('tweet', 'text')

    list_display = (
        'tweet',
        'text',
        're_tweet_count',
        'favorite_count',
        'created_at',
    )

    readonly_fields = ('created_at', 'favorite_count', 're_tweet_count')


admin.site.register(Tweet, TweetAdmin)
