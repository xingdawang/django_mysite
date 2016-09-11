from django.conf.urls import url
from .views import posts_home

urlpatterns = [
	url(r'^$', posts_home)
]