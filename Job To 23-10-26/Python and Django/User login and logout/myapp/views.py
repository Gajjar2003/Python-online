from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def index(request):
    return render(request, "index.html")


def user_register(request):

    if request.method == "POST":

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():

            return render(request, "index.html", {
                "err": "User already exists !!!"
            })

        else:

            u = User.objects.create(
                first_name=fname,
                last_name=lname,
                username=username
            )

            u.set_password(password)
            u.save()

            return render(request, "index.html", {
                "meg": "User registered successfully done !!!"
            })

    return render(request, "index.html")


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        u = authenticate(
            username=username,
            password=password
        )

        if u is None:

            return render(request, "user-login.html", {
                "err": "Invalid username and password !!!"
            })

        else:

            login(request, u)

            return redirect("home")

    return render(request, "user-login.html")


@login_required
def home(request):

    return render(request, "home.html")


def user_logout(request):

    logout(request)

    return redirect("user-login")