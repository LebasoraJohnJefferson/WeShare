from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def visitor_home(request):
    return render(request , 'visitorHome/visitor-home.html' , { 'lebs':'300' })

def loginPage(request):
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

    context={}
    return render(request , 'visitorHome/auth/login.html',context)

def signup(request):
    return render(request , 'visitorHome/auth/signup.html')

def profile(request):
    return render(request, 'visitorHome/profile.html')
