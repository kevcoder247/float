from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('home Page')


def about(request):
    return HttpResponse('About Page')