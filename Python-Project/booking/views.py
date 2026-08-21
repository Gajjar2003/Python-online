from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from booking.models import *

def index(request):
  return render(request,"index.html")


@login_required(login_url='user-login')
def book_now(request):
  return render(request,"book-now.html")

@login_required(login_url='user-login')
def my_booking(request):
  return render(request,"my-booking.html")

def about(request):
  return render(request,"about.html")

def service(request):
  return render(request,"service.html")

def user_register(request):

  if request.method == 'POST':
    
      fname = request.POST.get('fname')
      lname = request.POST.get('lname')
      email = request.POST.get('email')
      username = request.POST.get('username')
      password = request.POST.get('password')

      if User.objects.filter(username=username).exists():
        return render(request,"user-register.html",{'err':"Username already exists ??"})

      else:

        u = User.objects.create(first_name=fname,last_name=lname,email=email,username=username)
        u.set_password(password)
        u.save()

  return render(request,"user-register.html",{'meg':'User Craete Successfully !!!'})

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    u = authenticate(username=username,password=password)
    if u is None:
      return render(request,"user-login.html",{'err':'Invalid Username and password ???'})
    else:
      login(request,u)
      return redirect("index")

  return render(request,"user-login.html")

def user_logout(request):
  logout(request)
  return render(request,"user-login.html")


@login_required
def booking_form(request):

    if request.method == "POST":

        number = request.POST.get("number")
        slot_time = request.POST.get("slot_time")
        duration = request.POST.get("duration")
        payment_option = request.POST.get("payment_option")

        Booking.objects.create(
            user=request.user,
            email=request.user.email,
            number=number,
            slot_time=slot_time,
            duration=duration,
            payment_option=payment_option
        )

        return redirect("my-booking")

    return render(request, "booking-form.html")

