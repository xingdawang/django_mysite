from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'content', 'updated', 'timestamp']
	list_display_links = ['title', 'content']
	list_filter = ['updated', 'timestamp']
	# list_editable = ['title']
	search_fields = ['content']
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)