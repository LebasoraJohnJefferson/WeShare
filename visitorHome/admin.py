from django.contrib import admin
from . models import Post, Comment, Profile

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_owner','description','post_image','created','updated']
    list_filter = ['post_owner']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post_comment','user_comment','context_comment','created_at']
    list_filter = ['post_comment']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_profile','user_image','first_name','last_name','self_description']
    filter = ['user_profile']

