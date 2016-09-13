from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Post
from .forms import PostForm

def posts_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Successfully Created')
	else:
		messages.error(request, 'Not Successfully Created')
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
	return render(request, 'base.html', context)

def posts_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Item Updated", extra_tags='html_safe')
	context = {
		'title': 'Detail',
		'instance': instance,
		'form': form,
	}
	return render(request, 'post_form.html', context)

def posts_delete(request,id=id):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, 'Successfully Deleted')
	return redirect('list')