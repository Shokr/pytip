from django.urls import path

from .views import *

app_name = 'core'

urlpatterns = [
    path('', TweetListView.as_view(), name='home'),

    path('add/', TweetCreate.as_view(), name='tweet-add'),
    path('update/<int:pk>/', TweetUpdate.as_view(), name='tweet-update'),
    # path('delete/<int:pk>/', TweetDelete.as_view(), name='tweet-delete'),
    path('<int:pk>/', TweetDetailView.as_view(), name='tweet-detail'),

    path('search/', SearchResultsView.as_view(), name='search'),

]
