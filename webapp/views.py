from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

def index(request):
	return HttpResponse("Hello world!")
