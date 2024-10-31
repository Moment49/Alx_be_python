from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Home website")

def index(request):
    return HttpResponse("Welcome to my books store.")