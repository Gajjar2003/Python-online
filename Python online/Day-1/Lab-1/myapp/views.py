from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def phone(request):
    return render(request,"phone.html")

def help(request):
    return render(request,"help.html")