from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *



# Create your views here.
def index(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']


        if User.objects.filter(username=username).exists():
             return render(request,"index.html",{'err':'User already exists !!!'})
        
        else:   
        
            u =  User.objects.create(first_name=fname,last_name=lname,username=username)
            u.set_password(password)
            u.save()
            return render(request,"index.html",{'meg':'User register successfully done !!!'})
        
    return render(request,"index.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        u=authenticate(username=username,password=password)
        if u is None:
            return render(request,"user-login.html",{'err':'Invalid Username and Password'})
        else:
            login(request,u)
            return redirect('home')


    return render(request,"user-login.html")

@login_required(login_url='user-login')
def home(request):
        return render(request,"home.html")

@login_required(login_url='user-login')
def user_logout(request):
     logout(request)
     return render(request,"user-login.html")

def useradd(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    contact = request.POST.get('contact')

    Useradd.objects.create(name=name,email=email,age=age,contact=contact)

    return render(request,"home.html",{'meg':'Useradd Successfully Done!!!'})

def userview(request):
     users = Useradd.objects.all()
     return render(request,"userview.html",{'users':users})