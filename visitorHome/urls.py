from django.urls import path
from . import views

urlpatterns = [
    path('', views.visitor_home , name='visitor-home'),
]
