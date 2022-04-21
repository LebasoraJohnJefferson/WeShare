from atexit import register
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_owner = models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    post_image = models.ImageField(upload_to='images/posts/',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'posts'
        ordering = ('-updated',)
    def __int__(self):
        return self.post_owner
    def count_like(self):
        return self.like_post.filter(is_like=True)

class Likes(models.Model):
    #the post
    like_post = models.ForeignKey(Post,related_name='like_post',on_delete=models.CASCADE)
    #the liker of post
    liker = models.ForeignKey(User,related_name='liker',on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'Likes'
    def __bool__(self):
        return self.is_like

