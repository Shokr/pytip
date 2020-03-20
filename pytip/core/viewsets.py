from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import TweetSerializer, Tweet


class TweetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
