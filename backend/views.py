from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Link, Topic
from .serializers import *

@csrf_exempt
def topicLinks(request,topic):
    """
    List all links
    """
    if request.method == 'GET':
        links = Link.objects.filter(topic__name=topic)
        serializer = LinkSerializer(links, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
