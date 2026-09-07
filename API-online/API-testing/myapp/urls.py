from django.urls import path
from myapp.views import *

urlpatterns = [
  path('get-api',get_api,name="get-api")
]