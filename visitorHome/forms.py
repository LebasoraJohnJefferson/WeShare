from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import Post


class UserForm(ModelForm):
    class Meta:
        model=User
        fields = ['email','password']

class PostImageFrom(ModelForm):
    class Meta:
        model = Post
        fields = ['description','post_image']