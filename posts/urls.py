from django.conf.urls import url
from . import views

app_name = 'posts'	# need to add the namespace in the template file
urlpatterns = [
	url(r'^$', views.posts_list),
	url(r'^create/$', views.posts_create),
	url(r'^(?P<id>\d+)/$', views.posts_detail, name='detail'),
	url(r'^(?P<id>\d+)/edit/$', views.posts_update, name='update'),
	url(r'^delete/$', views.posts_delete),
]