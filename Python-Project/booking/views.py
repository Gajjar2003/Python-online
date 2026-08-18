from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from booking.models import Booking


# ==========================================
# HOME / INDEX
# ==========================================

def index(request):

    slots = [
        {
            "time": "05:00 PM",
            "hour": 17,
            "period": "Evening"
        },
        {
            "time": "06:00 PM",
            "hour": 18,
            "period": "Evening"
        },
        {
            "time": "07:00 PM",
            "hour": 19,
            "period": "Evening"
        },
        {
            "time": "08:00 PM",
            "hour": 20,
            "period": "Night"
        },
        {
            "time": "09:00 PM",
            "hour": 21,
            "period": "Night"
        },
        {
            "time": "10:00 PM",
            "hour": 22,
            "period": "Night"
        },
        {
            "time": "11:00 PM",
            "hour": 23,
            "period": "Night"
        },
        {
            "time": "12:00 AM",
            "hour": 24,
            "period": "Midnight"
        },
        {
            "time": "01:00 AM",
            "hour": 25,
            "period": "Late Night"
        },
        {
            "time": "02:00 AM",
            "hour": 26,
            "period": "Closing Time"
        }
    ]

    return render(
        request,
        "index.html",
        {
            "slots": slots
        }
    )


# ==========================================
# USER REGISTER
# ==========================================

def user_register(request):

    if request.method == "POST":

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check username
        if User.objects.filter(username=username).exists():

            return render(
                request,
                "user-register.html",
                {
                    "err": "Username already exists!"
                }
            )

        # Create user
        user = User.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            username=username
        )

        user.set_password(password)
        user.save()

        return render(
            request,
            "user-register.html",
            {
                "meg": "User registered successfully!"
            }
        )

    return render(request, "user-register.html")


# ==========================================
# USER LOGIN
# ==========================================

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:

            return render(
                request,
                "user-login.html",
                {
                    "err": "Invalid Username & Password!"
                }
            )

        login(request, user)

        return redirect("index")

    return render(request, "user-login.html")


# ==========================================
# USER LOGOUT
# ==========================================

def user_logout(request):

    logout(request)

    return redirect("user-login")


# ==========================================
# BOOK SLOT
# ==========================================

@login_required
def book_slot(request):

    if request.method == "POST":

        start_time = request.POST.get("start_time")
        start_hour = int(request.POST.get("start_hour"))
        duration = int(request.POST.get("duration"))

        # Closing time = 2 AM
        closing_hour = 26

        # Check duration
        if start_hour + duration > closing_hour:

            return render(
                request,
                "error.html",
                {
                    "message": "This duration is not available. "
                               "Box Cricket closing time is 2:00 AM."
                }
            )

        # Price
        price = 700 * duration

        # Save booking
        Booking.objects.create(
            user=request.user,
            start_time=start_time,
            duration=duration,
            price=price
        )

        return redirect("my-booking")

    return redirect("index")


# ==========================================
# MY BOOKING
# ==========================================

@login_required
def my_booking(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "my_booking.html",
        {
            "bookings": bookings
        }
    )