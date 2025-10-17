from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#Funtion based view

def home(request):
    return HttpResponse("Welcome to Django App")

def index(request):
    return HttpResponse("Index page")
