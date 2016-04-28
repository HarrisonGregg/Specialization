"""Specialization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from backend.models import Topic, Link
from rest_framework import routers, serializers, viewsets

import backend.views
from backend.serializers import *

router = routers.DefaultRouter()
router.register(r'^topics', TopicViewSet)
router.register(r'^links', LinkViewSet)
router.register(r'^trajectories', TrajectoryViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^search/(?P<search_string>.*)/$', backend.views.searchTopics, name='search'),
    url(r'^topicLinks/(?P<topic_name>.*)/$', backend.views.topicLinks, name='links'),
	url(r'^getTopic/(?P<topic_name>.*)/$', backend.views.getTopic, name='getTopic'),
	url(r'^upvote/(?P<link_pk>.*)/$', backend.views.upvote, name='upvote'),
	url(r'^downvote/(?P<link_pk>.*)/$', backend.views.downvote, name='downvote'),
	# url(r'^link/(?P<pk>.*)/$', backend.views.link, name='link'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^signup/$', backend.views.signup, name='signup'),
    url(r'^signin/$', backend.views.signin, name='signin'),
]
