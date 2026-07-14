from django.urls import path
from Simple_crud.myapp.views import  *

urlpatterns= [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("delete",delete,name="delete"),
    path("edit",edit,name="edit")
]