from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>Welcome to the blog!</h1>')

# def about(request):
#     return HttpResponse('<h1>About Page of the blog</h1>')

posts = [
    {
    'author': 'Krishna Swaroop',
    'title': 'Blog Post 1',
    'date_posted': 'June 3, 2020',
    'content': 'First Blog post content'
    },
    {
    'author': 'John Doe',
    'title': 'Blog Post 2',
    'date_posted': 'June 3, 2020',
    'content': 'Second Blog post content'
    }
]

def home(request):
    context = {
        'key': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    jsonDict = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', jsonDict)