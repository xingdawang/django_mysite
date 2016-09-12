from django.conf.urls import url
from . import views

app_name = 'posts'	# need to add the namespace in the template file
urlpatterns = [
	url(r'^create/$', views.posts_create),
	url(r'^detail/$', views.posts_detail),
	url(r'^list/$', views.posts_list),
	url(r'^update/$', views.posts_update),
	url(r'^delete/$', views.posts_delete),
]