from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
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

    Links = getLink('Home')

    return render(request , 'visitorHome/visitor-home.html' , { 
        'lebs':'300',
        'Links':Links
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
