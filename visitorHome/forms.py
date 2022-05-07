from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import Post, Profile


class UserForm(ModelForm):
    class Meta:
        model=User
        fields = ['email','password']

class PostImageFrom(ModelForm):
    class Meta:
        model = Post
        fields = ['id','description','post_image']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user_image','first_name','last_name','self_description']