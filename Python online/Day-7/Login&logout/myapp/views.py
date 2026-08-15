from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,"index.html")

def register(request):

    if request.method == "POST":

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        password = request.POST.get("password")

       # Check username already exists
        if User.objects.filter(username=username).exists():

            return render(
                request,
                "index.html",
                {"err": "Username already exists!"}
            )

        # Create User
        user = User.objects.create_user(
            first_name=fname,
            last_name=lname,
            username=username,
            password=password
        )

        return render(
            request,
            "index.html",
            {"msg": "Registration Successful!"}
        )

    return render(request, "index.html")


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

      
        u = authenticate(username=username,password=password)
        if u is None:
          return render(request,"user-login.html",{'err':"invalid Username and password ???"})
        else:
            login(request,u)
            return redirect("home")

    

    return render(request, "user-login.html")

@login_required(login_url="user-login")
def home(request):
    return render(request, "home.html")

def user_logout(request):
    logout(request)
    return render(request,"user-login.html")

