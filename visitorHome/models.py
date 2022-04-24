from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_owner = models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    liked = models.ManyToManyField(User,related_name='liked')
    description = models.TextField(blank=True)
    post_image = models.ImageField(upload_to='images/posts/',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'posts'
        ordering = ('-updated',)
    def __int__(self):
        return self.post_owner

