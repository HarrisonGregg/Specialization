from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from .models import Topic, Link

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('name',)

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class LinkSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(required=False)

    class Meta:
        model = Link
        fields = ('url','score','pk','topic')

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer