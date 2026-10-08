from django.urls import path
from myapp.views import *

urlpatterns = [
  path("",index,name="index"),
  path("user-register",user_register,name="user-register"),
  path("user-login",user_login,name="user-login"),
  path("home",home,name="home"),
  path("user-logout",user_logout,name="user-logout")
]