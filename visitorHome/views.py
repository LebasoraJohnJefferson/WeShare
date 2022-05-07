from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from . models import Post, Comment,Profile
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
            Profile.objects.create(user_profile = user)
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
    all_post = Post.objects.get(id=post_pk)
    if request.user.is_authenticated:
        if request.user in all_post.liked.all():
            all_post.liked.remove(request.user)
        else:
            all_post.liked.add(request.user)
    else:
        messages.warning(request,'Visitor request is prohibited!')
    return redirect(request.META.get('HTTP_REFERER'))


def commentPage(request,post_pk):
    try:
        posts = Post.objects.filter(id = post_pk)
        if request.user.is_authenticated:
            Links=[]
            if request.method == 'POST':
                if request.POST.get('comment').strip() != '':
                    Comment.objects.create(
                        post_comment = Post.objects.get(id=post_pk),
                        user_comment = request.user,
                        context_comment = request.POST.get('comment')
                    )
                else:
                    messages.warning(request,'Comment is empty!')
        else:
            Links = getLink('Home')
    except:
            messages.error(request,'No Post Found')
            posts=[]
            
    return render(request,'visitorHome/visitor-home.html',{
        'posts':posts,
        'show_post_form':True,
        'Links':Links,
    })

@login_required(login_url='Login')
def profile(request,get_username):
    if request.user.is_authenticated:
        try:
            current_user = User.objects.get(username=get_username)
        except:
            current_user=0
        if current_user == 0:
            messages.error(request,get_username+' Does not Exist!')
            return redirect('visitor-home')
        profile_info = Profile.objects.get(user_profile=current_user)
        posts = Post.objects.filter(post_owner = current_user)
        likes = Post.objects.filter(liked=current_user).count()
        comments = Comment.objects.filter(user_comment=current_user).count()
        number_posts = Post.objects.filter(post_owner=current_user).count()
    return render(request, 'visitorHome/profile.html',{
        'show_post_form':True,
        'hide_comment':True,
        'profile_info':profile_info,
        'posts':posts,
        'likes':likes,
        'comments':comments,
        'number_posts':number_posts
})





