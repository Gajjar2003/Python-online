from django.urls import path
from booking.views import *

urlpatterns = [
  path("",index,name="index")
]