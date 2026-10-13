
from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="user-login"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("user-logout/", views.user_logout, name="user-logout"),
]