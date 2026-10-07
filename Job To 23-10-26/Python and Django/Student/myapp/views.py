from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
  return render(request,"index.html")


def register(request):
  id = request.POST.get("id")
  name = request.POST.get("name")
  age = request.POST.get("age")
  email = request.POST.get("email")
  number = request.POST.get("number")

  if not id:
      Student.objects.create(name=name,age=age,email=email,number=number)
      return render(request,"index.html",{'meg':"Student Registered Successfully!"})
  else:
      s = Student.objects.get(id=id)
      s.name=name
      s.age=age
      s.email=email
      s.number=number
      s.save()
      return render(request,"index.html",{'meg':"Student Update Successfully!"})


def display(request):
  students = Student.objects.all()
  return render(request,"display.html",{'students':students})

def delete(request):
  id  = request.GET.get("id")
  s = Student.objects.get(id=id)
  s.delete()
  return redirect("display")

def edit(request):
  id  = request.GET.get("id")
  s = Student.objects.get(id=id)
  return render(request,"index.html",{'s':s})