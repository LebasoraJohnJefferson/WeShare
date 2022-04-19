from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from . models import Post
from .forms import PostImageFrom
# from PIL import Image
# Create your views here.

#header navigation links
header_links = [
    {'text':'Login','url':'Login'},
    {'text':'Sign up','url':'Signup'},
    {'text':'Home','url':'visitor-home'},
]
#header function to ignore links that not necessary
def getLink(text):
    temp_list=[]
    for link_list in header_links:
        if link_list['text']==text:
            pass
        else:
            temp_list.append(link_list)
    return temp_list

def visitor_home(request):
    posts = Post.objects.all()
    Links = getLink('Home')
    form = PostImageFrom()

    return render(request , 'visitorHome/visitor-home.html' , { 
        'posts':posts,
        'Links':Links,
        'form':form
     })


def signup(request):
    form = UserCreationForm()
    Links = getLink('Sign up')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('visitor-home')
        else:
            messages.error(request, 'An Error Occurred during registration!')
    return render(request , 'visitorHome/auth/signup.html' , {
        'Links':Links,
        'form':form
    })

def loginPage(request):
    Links = getLink('Login')
    if request.method == 'POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"Account does not Exist")
            return redirect('Login')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('visitor-home')
        else:
            messages.error(request,"Account does not Exist")
            return redirect('Login')

    return render(request , 'visitorHome/auth/login.html',{ 
        'Links':Links,
        'is_show_option':True
    })


def logoutPage(request):
    logout(request)
    return redirect('visitor-home')


def profile(request):
    return render(request, 'visitorHome/profile.html',{
        
    })

def post(request):
    form = PostImageFrom(request.POST, request.FILES)
    if request.method == 'POST':
        if (request.POST.get('description').strip() !='' or request.POST.get('post_image')!=''):
            if form.is_valid():
                post = form.save(commit=False)
                post.post_owner = request.user
                post.save()
            else:
                messages.error(request,'Invalid image')
        else:
            messages.warning(request,'Say something..!!')
    else:
        messages.error(request,'Error Data!!')
    return redirect('visitor-home')

def deletePost(request,post_pk):
    try:
        post = Post.objects.get(id=post_pk)
        if post.post_owner.id == request.user.id:
            post.delete()
        else:
            messages.warning(request,'Request Denied!')
    except:
        messages.error(request,'No Post Found')
    return redirect('visitor-home')

def editPage(request,post_pk):
    messages.success(request,post_pk)
    return redirect('visitor-home')
