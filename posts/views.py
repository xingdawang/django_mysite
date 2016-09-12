from django.shortcuts import render
from django.http import HttpResponse

def posts_create(request):
	return HttpResponse('hello world');

def posts_detail(request):	#retrieve
	context = {
		'title': 'Detail'
	}
	return render(request, 'index.html', context)

def posts_list(request):	#list items
	if request.user.is_authenticated():
		context = {
			'title': 'User is authenticated'
		}
	else:
		context = {
			'title': 'User is not authenticated'
		}
	return render(request, 'index.html', context)

def posts_update(request):
	return HttpResponse('hello world');

def posts_delete(request):
	return HttpResponse('hello world');