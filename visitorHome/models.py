from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile = models.ImageField(upload_to="images/profiles")
    slug = models.SlugField(max_length=255)
    is_active=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="Users_Fields"

    def __str__(self):
        return self.user