from django.contrib import admin
from . models import Post, Likes

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_owner','description','post_image','created','updated']
    list_filter = ['post_owner']

@admin.register(Likes)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['like_post','liker','is_like']
    class Meta:
        verbose_name_plural = 'Likes'
    def __int__(self):
        return self.id

