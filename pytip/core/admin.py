from django.contrib import admin

from .froms import TweetForm
from .models import *


class TweetAdmin(admin.ModelAdmin):
    form = TweetForm

    search_fields = ('tweet', 'text')

    list_display = (
        'tweet',
        'text',
        'retweet_count',
        'favorite_count',
        'created_at',
    )

    readonly_fields = ('created_at', 'favorite_count', 'retweet_count')


admin.site.register(Tweet, TweetAdmin)

admin.site.register(Url)
admin.site.register(Image)
admin.site.register(Hashtag)
