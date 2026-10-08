from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
  return render(request,"index.html")


def register(request):
  id = request.POST.get("id")
  name= request.POST.get("name")
  age= request.POST.get("age")
  email = request.POST.get('email')
  number = request.POST.get("number")
  city = request.POST.get("city")

  if not id:
      Employee .objects.create(name=name,email=email,age=age,number=number,city=city)
      return render(request,"index.html",{'meg':'Successfully done !!!'})
  else:
    e = Employee.objects.get(id=id)
    e.name=name
    e.age=age
    e.email=email
    e.number =number
    e.city=city
    e.save()


    return render(request,"index.html",{'meg':'Successfully Updated done !!!'})

def display(request):
  employee = Employee.objects.all()
  return render(request,"display.html",{'employee':employee})

def delete(request):
  id = request.GET.get("id")
  e = Employee.objects.get(id=id)
  e.delete()
  return redirect("display")


def edit(request):
  id = request.GET.get("id")
  e = Employee.objects.get(id=id)
  return render(request,"index.html",{'e':e})