from django .urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name= "index"),
    path("user-login",user_login,name="user-login"),
    path('home',home,name='home'),
    path("user-logout",user_logout,name="user-logout"),
    path("useradd",useradd,name="useradd"),
    path("userview",userview,name="userview")
]