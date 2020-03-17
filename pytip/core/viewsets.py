from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes

from .serializers import TweetSerializer, Tweet


@permission_classes((permissions.AllowAny,))
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
