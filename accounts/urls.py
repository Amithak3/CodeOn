from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('', views.home, name='home'),  # Home page redirection
     path('logout/', views.logoutPageView, name='logoutPage'),
    path('problems/', views.problemPageView, name='problemPage'),
    path('discussions/', views.discussionPageView, name='discussionPage'),
]
