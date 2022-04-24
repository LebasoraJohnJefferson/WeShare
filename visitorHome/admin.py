from django.contrib import admin
from . models import Post, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_owner','description','post_image','created','updated']
    list_filter = ['post_owner']

@admin.register(Comment)
class CommentPost(admin.ModelAdmin):
    list_display = ['post_comment','user_comment','context_comment','created_at']
    list_filter = ['post_comment']

