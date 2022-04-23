from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from . models import Post, Likes
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
    que=request.GET.get('que') if request.GET.get('que') != None else ''
    posts = Post.objects.filter(Q(description__icontains=que)|
                                Q(post_owner__username__icontains=que)
                                )
    Links = getLink('Home')
    return render(request , 'visitorHome/visitor-home.html' , { 
        'posts':posts,
        'Links':Links,
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
            messages.error(request, 'Invalid Information!')
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

@login_required(login_url='Login')
def logoutPage(request):
    logout(request)
    return redirect('visitor-home')

@login_required(login_url='Login')
def profile(request):
    return render(request, 'visitorHome/profile.html',{
    })

@login_required(login_url='Login')
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

@login_required(login_url='Login')
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

@login_required(login_url='Login')
def editPage(request,post_pk):
    current_post = Post.objects.get(id=post_pk)
    if request.method == "POST":
        if (request.POST.get('description').strip() !='' or request.POST.get('post_image')!=''):
            update_post = PostImageFrom(request.POST,request.FILES,instance=current_post)
            if update_post.is_valid():
                update_post.save()
                return redirect('visitor-home')
            else:
                messages.warning(request,"Request Denied!!")
        else:
            messages.warning(request,"Request Denied!!")

    return render(request,'visitorHome/edit-page.html',{
        'post':current_post,
        'post_pk': post_pk
    })

@login_required(login_url='Login')
def likePage(request,post_pk):
    id = request.user.id
    if request.user.is_authenticated:
        if_user_exist = Likes.objects.filter(liker=id,like_post=post_pk)
        if if_user_exist:
            like = Likes.objects.get(liker=id,like_post=post_pk)
            like.is_like = False if like.is_like else True
            like.save()
        else:
            get_post = Post.objects.get(id=post_pk)
            get_user = User.objects.get(id=id)
            Likes.objects.create(
                like_post = get_post,
                liker = get_user,
                is_like = True
            )
    else:
        messages.warning(request,'Visitor request is prohibited!')
    return redirect('visitor-home')

def commentPage(request,post_pk):
    posts = Post.objects.filter(id = post_pk)
    is_user_like = Likes.objects.filter(liker=request.user.id,is_like=True)  
    return render(request,'visitorHome/comment-page.html',{
        'posts':posts,
        'show_post_form':True,
        'is_user_like':is_user_like
    })




