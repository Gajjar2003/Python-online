from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from  django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  return render(request,"index.html")

def register(request):
  fname = request.POST.get('fname')
  lname = request.POST.get('lname')
  username = request.POST.get('username')
  password = request.POST.get('password')

  if User.objects.filter(username=username).exists():
      return render(request,"index.html",{'err':'User already Exsists ???'})

  else:
    u =  User.objects.create(first_name=fname,last_name=lname,username=username)
    u.set_password(password)
    u.save()

  return render(request,"index.html",{'msg':'User Register successfully Done !!!'})

def user_login(request):
  username = request.POST.get('username')
  password = request.POST.get('password')

  u = authenticate(username=username,password=password)
  if u is None:
    return render(request,"user-login.html",{'err':'Invalid Username and password ??'})
  else:
    login(request,u)
    return redirect("home")
  
  return render(request,"user-login.html")

def home(request):
  return render(request,"home.html")

def user_logout(request):
  logout(request)
  return render(request,"user-login.html")