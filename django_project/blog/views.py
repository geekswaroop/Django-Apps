from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to the blog!</h1>')

def about(request):
    return HttpResponse('<h1>About Page of the blog</h1>')