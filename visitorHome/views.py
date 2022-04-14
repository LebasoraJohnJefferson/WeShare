from django.shortcuts import render

# Create your views here.

def visitor_home(request):
    return render(request , 'visitorHome/visitor-home.html' , { 'lebs':'20' })
