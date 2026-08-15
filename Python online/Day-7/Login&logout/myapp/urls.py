from django.urls import path
from myapp.views import *

urlpatterns = [
  path("",index,name="index"),
  path("register",register,name="register"),
  path("user-login",user_login,name="user-login"),
  path("home",home,name="home"),
  path("user-logout",user_logout,name="user-logout")
]