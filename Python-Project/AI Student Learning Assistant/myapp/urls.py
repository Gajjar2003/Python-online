
from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", user_login, name="user-login"),
    path("register/", register, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("user-logout/", user_logout, name="user-logout"),
    path("ai-chat/", ai_chat, name="ai-chat"),
    path("ai-quiz/", ai_quiz, name="ai-quiz"),
    path("smart-notes/", ai_notes, name="ai-notes"),
    path("learning-progress/",learning_progress,name="learning-progress"),


   


]