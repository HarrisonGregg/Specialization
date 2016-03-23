from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Link, Topic
from .serializers import *

@csrf_exempt
def getTopic(request,topic_name):
	"""
	Return the topic object from the name
	"""
	if request.method == 'GET':
		topic = Topic.objects.get(name=topic_name)
		serializer = TopicSerializer(topic, context={'request': request})
		return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def searchTopics(request,search_string):
	"""
	Return a list of topics based on the search
	"""
	if request.method == 'GET':
		topics = Topic.objects.all()#filter(name__icontains=search_string)
		serializer = TopicSerializer(topics, many=True, context={'request': request})
		return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def topicLinks(request,topic_name):
	"""
	List all links
	"""
	if request.method == 'GET':
		links = Link.objects.filter(topic__name=topic_name).order_by('-score')
		serializer = LinkSerializer(links, many=True, context={'request': request})
		return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def upvote(request,link_pk):
	"""
	Increment the score for a link
	"""
	if request.method == 'PUT':
		link = Link.objects.get(pk=link_pk)
		link.score += 1
		link.save()
		serializer = LinkSerializer(link, context={'request': request})
		return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def downvote(request,link_pk):
	"""
	Increment the score for a link
	"""
	if request.method == 'PUT':
		link = Link.objects.get(pk=link_pk)
		link.score -= 1
		link.save()
		serializer = LinkSerializer(link, context={'request': request})
		return JsonResponse(serializer.data, safe=False)

