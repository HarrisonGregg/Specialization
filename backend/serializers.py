from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from django_comments.models import Comment

from .models import Trajectory, Level, Topic, Link#, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user_name', 'comment', 'submit_date', 'is_removed')

class TopicSerializer(serializers.ModelSerializer):
    link_count = serializers.IntegerField(source='count_links', read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ('name','pk','link_count')#,'comments')

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class LinkSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(required=False)

    class Meta:
        model = Link
        fields = ('url','score','pk','topic','title','date_added')

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class LevelSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Level
        fields = ('name','topics')

class TrajectorySerializer(serializers.ModelSerializer):
    levels = LevelSerializer(many=True, read_only=True)

    class Meta:
        model = Trajectory
        fields = ('pk','name','levels')

class TrajectoryViewSet(viewsets.ModelViewSet):
    queryset = Trajectory.objects.all()
    serializer_class = TrajectorySerializer

