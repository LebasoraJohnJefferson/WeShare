from django.shortcuts import render

# Create your views here.

def visitor_home(request):
    return render(request , 'visitorHome/visitor-home.html' , { 'lebs':'300' })

def login(request):
    return render(request , 'auth/login.html')

def signup(request):
    return render(request , 'auth/signup.html')
