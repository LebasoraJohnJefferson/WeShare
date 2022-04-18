from django.contrib import admin
from . models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_owner','description','post_image','created','updated']
    list_filter = ['post_owner']

