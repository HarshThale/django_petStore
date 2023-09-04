from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('this is an index page of petstore')

def products(request):
    return HttpResponse('<h1>Product page<h1>')