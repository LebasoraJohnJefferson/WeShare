from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
# Create your views here.

#header navigation links
header_links = [
    {'text':'Login','url':'Login'},
    {'text':'Sign up','url':'Signup'},
    {'text':'Home','url':'visitor-home'},
]
#header function to ignore links
def getLink(text):
    temp_list=[]
    for link_list in header_links:
        if link_list['text']==text:
            pass
        else:
            temp_list.append(link_list)
    return temp_list

def visitor_home(request):

    Links = getLink('Home')

    return render(request , 'visitorHome/visitor-home.html' , { 
        'lebs':'300',
        'is_show_option':True,
        'Links':Links
     })


def signup(request):
    Links = getLink('Sign up')
    return render(request , 'visitorHome/auth/signup.html' , {
        'is_show_option':True,
        'Links':Links
    })

def loginPage(request):
    Links = getLink('Login')
    if request.method == 'POST':
        username=request.POST.get('username')
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
        'is_show_option':False
    })
