from django.urls import path

from .views import *

app_name = 'core'

urlpatterns = [
    path('', listTweets, name='home'),

    path('tweet/add', addTweet, name='addTweet'),
    path('tweet/edit/<int:pk>/', editTweet, name='editTweet'),
    path('tweet/delete/<int:pk>/', deleteTweet, name='deleteTweet'),
    path('<int:pk>', viewTweet, name='viewTweet'),
]
