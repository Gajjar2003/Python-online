from django.urls import path
from myapp.views import *

urlpatterns = [
  path("",index,name="index"),
  path("add",add,name="add"),
  path("display",display,name="display"),
  path("delete",delete,name="delete"),
  path("edit",edit,name="edit")
]