from django.conf.urls import url
from .views import posts_home

app_name = 'posts'	# need to add the namespace in the template file
urlpatterns = [
	url(r'^$', posts_home)
]