from django.shortcuts import render

def index(request):
  return render(request,"index.html")


def book_now(request):
  return render(request,"book-now.html")


def my_booking(request):
  return render(request,"my-booking.html")

def about(request):
  return render(request,"about.html")

def service(request):
  return render(request,"service.html")

def user_register(request):
  return render(request,"user-register.html")

def user_login(request):
  return render(request,"user-login.html")

