from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('loggedin', views.loggedin, name='loggedin'),
    path('logout', views.logout, name='logout'),
]