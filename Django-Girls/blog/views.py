from django.shortcuts import render

# Create your views here.
#post_list is a function which takes a request and returns back another function
def post_list(request):
	return render(request, 'blog/post_list.html',{})

