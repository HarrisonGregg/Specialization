from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth        import authenticate, login, logout
from django_comments.models import Comment
from django.views.decorators.http import require_POST

from django import http
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import escape

import django_comments
from django_comments import signals
from django_comments.views.utils import next_redirect, confirmation_view
from django_comments.views.comments import CommentPostBadRequest

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Link, Topic
from .serializers import *

def getComments(request,model,id):
    comments = Comment.objects.filter(object_pk=id,content_type__model=model)

    serializer = CommentSerializer(comments, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)

# def addComment(request,model,id):
#   comment = Comment(content_type=model,object_pk=id)  

#   serializer = CommentSerializer(comments, many=True, context={'request': request})
#   return JsonResponse(serializer.data, safe=False)

@require_POST
def post_comment(request, next=None, using=None):
    """
    Post a comment.
    HTTP POST is required. If ``POST['submit'] == "preview"`` or if there are
    errors a preview template, ``comments/preview.html``, will be rendered.
    """
    # Fill out some initial data fields from an authenticated user, if present
    data = request.POST.copy()
    if request.user.is_authenticated():
        if not data.get('name', ''):
            data["name"] = request.user.get_full_name() or request.user.get_username()
        if not data.get('email', ''):
            data["email"] = request.user.email

    # Look up the object we're trying to comment about
    ctype = data.get("content_type")
    object_pk = data.get("object_pk")
    if ctype is None or object_pk is None:
        return CommentPostBadRequest("Missing content_type or object_pk field.")
    try:
        model = apps.get_model("backend",ctype)
        # model = apps.get_model(*ctype.split(".", 1))
        target = model._default_manager.using(using).get(pk=object_pk)
    except TypeError:
        return CommentPostBadRequest(
            "Invalid content_type value: %r" % escape(ctype))
    except AttributeError:
        return CommentPostBadRequest(
            "The given content-type %r does not resolve to a valid model." % escape(ctype))
    except ObjectDoesNotExist:
        return CommentPostBadRequest(
            "No object matching content-type %r and object PK %r exists." % (
                escape(ctype), escape(object_pk)))
    except (ValueError, ValidationError) as e:
        return CommentPostBadRequest(
            "Attempting go get content-type %r and object PK %r exists raised %s" % (
                escape(ctype), escape(object_pk), e.__class__.__name__))

    # Create the comment
    comment = Comment(
        content_object=target,
        user_name=data["name"],
        user_email=data["email"],
        comment=data["comment"],
        site_id=settings.SITE_ID
    )
    comment.ip_address = request.META.get("REMOTE_ADDR", None)
    if request.user.is_authenticated():
        comment.user = request.user

    # Signal that the comment is about to be saved
    responses = signals.comment_will_be_posted.send(
        sender=comment.__class__,
        comment=comment,
        request=request
    )

    for (receiver, response) in responses:
        if response is False:
            return CommentPostBadRequest(
                "comment_will_be_posted receiver %r killed the comment" % receiver.__name__)

    # Save the comment and signal that it was saved
    comment.save()
    signals.comment_was_posted.send(
        sender=comment.__class__,
        comment=comment,
        request=request
    )

    serializer = CommentSerializer(comment, context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def currentUser(request):
    """
    Check if a user is logged in and get their username
    """
    if request.user.is_authenticated():
        print(request.user.username)
        return HttpResponse(request.user.username)
    return HttpResponseBadRequest("no user logged in")

# @csrf_exempt
# def comment(request):
#   """
#   Add a comment
#   """
#   if request.method == 'POST':
#       topic_id = request.POST["topic_id"]
#       text = request.POST["text"]
#       user = User.objects.get(id=1)
#       comment = Comment(text=text,user=user)
#       comment.save()
#       topic = Topic.objects.get(id=topic_id)
#       topic.comments.add(comment)

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

@csrf_exempt
def signup(request):
    """
    Create a new user account
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("Use a POST request to create an account.")
    try:
        username     = request.POST["username"]
        email        = request.POST["email"]
        password     = request.POST["password"]
    except:
        return HttpResponseBadRequest("Fields missing.")

    try: 
        user.objects.get(username=username)
        return HttpResponseBadRequest("An account with that username already exists.")
    except:
        pass

    try:
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password, 
        )
        user.save()
    except:
        return HttpResponseBadRequest("An account with that email already exists.")
    return HttpResponse("Account created.")


@csrf_exempt
def signin(request):
    """
    Log a user in
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("Use a POST request to login.")

    try:
        username     = request.POST["username"]
        password     = request.POST["password"]
    except:
        return HttpResponseBadRequest("Please include a username and password.")

    user = authenticate(username=username, password=password)
    if not user or not user.is_active:
        return HttpResponseBadRequest("Invalid username or password.")

    login(request, user)
    return HttpResponse("Logged in.")

