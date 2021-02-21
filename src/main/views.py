from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return HttpResponse("<h1> Welcome </h1>")
    
def index(response):
    return HttpResponse("<h1>Index</h1>")