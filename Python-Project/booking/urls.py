from django.urls import path
from booking.views import *

urlpatterns = [

    path("", index, name="index"),

    path("user-register/", user_register, name="user-register"),

    path("user-login/", user_login, name="user-login"),

    path("user-logout/", user_logout, name="user-logout"),

    path("book-slot/", book_slot, name="book-slot"),

    path("my-booking/", my_booking, name="my-booking"),

]