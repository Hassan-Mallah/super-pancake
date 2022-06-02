from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    text = 'welcome to index'
    return HttpResponse(text)
