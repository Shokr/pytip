from rest_framework import viewsets

from .serializers import TweetSerializer, Tweet


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
