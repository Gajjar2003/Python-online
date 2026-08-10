from django.urls import path
from empapp.views import *

urlpatterns = [
    path('dept/',deptApi.as_view()),
    path("dept/<id>",deptupdate.as_view()),

      

]