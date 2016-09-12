from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

def posts_create(request):
	return HttpResponse('hello world');

def posts_detail(request):	#retrieve
	instance = get_object_or_404(Post, id=1)
	context = {
		'title': 'Detail',
		'instance': instance,
	}
	return render(request, 'detail.html', context)

def posts_list(request):	#list items
	queryset = Post.objects.all()
	context = {
		'object_list': queryset,
		'title': 'User is not authenticated'
	}
	return render(request, 'index.html', context)

def posts_update(request):
	return HttpResponse('hello world');

def posts_delete(request):
	return HttpResponse('hello world');