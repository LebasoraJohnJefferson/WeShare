from django.urls import path
from . import views

urlpatterns = [
    path('', views.visitor_home , name='visitor-home'),
    path('login', views.loginPage , name="Login"),
    path('logout', views.logoutPage , name="Logout"),
    path('signup', views.signup , name="Signup"),

    path('profile/<str:get_username>', views.profile , name="profile"),
    path('profile-info/edit', views.editProfile , name="edit-profile"),

    path('post', views.post , name="post"),
    path("post/delete/<str:post_pk>", views.deletePost , name="delete"),
    path("post/like/<str:post_pk>/", views.likePage , name="likes"),
    path("post/comment/<str:post_pk>/", views.commentPage , name="comment"),
    path("post/edit/<str:post_pk>/", views.editPage , name="edit"),
]
