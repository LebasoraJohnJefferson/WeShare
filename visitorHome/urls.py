from django.urls import path
from . import views

urlpatterns = [
    path('', views.visitor_home , name='visitor-home'),
    path('login', views.loginPage , name="Login"),
    path('signup', views.signup , name="Signup"),
    path('profile', views.profile , name="Profile"),
]
