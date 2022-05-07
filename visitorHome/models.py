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
    def number_of_comment(self):
        return self.post_comment.all()

class Comment(models.Model):
    post_comment = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comment')
    user_comment = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    context_comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'comments'
        ordering = ('-created_at',)


class Profile(models.Model):
    user_profile = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='user_profile')
    user_image = models.ImageField(upload_to='images/profiles_image/',null=True,blank=True)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    self_description = models.TextField(max_length=255)
    class Meta:
        verbose_name_plural = 'user_profiles'
    def __str__(self):
        if (self.first_name and self.last_name):
            return self.first_name+ " " + self.last_name
        else:
            return self.user_profile.username
