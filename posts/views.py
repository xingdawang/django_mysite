from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post
from .forms import PostForm

def posts_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	# if request.method == 'POST':
	# 	print request.POST
	context = {
		'form': form
	}
	return render(request, 'post_form.html', context)

def posts_detail(request, id=id):	#retrieve
	instance = get_object_or_404(Post, id=id)
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

def posts_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		'title': 'Detail',
		'instance': instance,
		'form': form,
	}
	return render(request, 'post_form.html', context)

def posts_delete(request):
	return HttpResponse('hello world')