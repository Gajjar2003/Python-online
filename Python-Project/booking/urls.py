from django.urls import path
from booking.views import *

urlpatterns = [ 
  path("",index,name="index"),
  path("book-now",book_now,name="book_now"),
  path("my-booking",my_booking,name="my-booking"),
  path("about",about,name="about"),
  path("service",service,name="service"),
  path("user-register",user_register,name="user-register"),
  path("user-login",user_login,name="user-login")
  

]