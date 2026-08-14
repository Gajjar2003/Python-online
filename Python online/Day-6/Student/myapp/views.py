from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
  return render(request,'index.html')

def register(request):
  id = request.POST.get('id')
  name = request.POST.get('name')
  email = request.POST.get('email')
  age = request.POST.get('age')
  subject = request.POST.get('subject')
  marks = request.POST.get('marks')

  if not id:
    Student.objects.create(name=name,email=email,age=age,subject=subject,marks=marks)
    return render(request,"index.html",{'msg':'Student Registered Successfully'})

  else:
      s = Student.objects.get(id=id)
      s.name=name
      s.email=email
      s.age=age
      s.subject=subject
      s.marks=marks
      s.save()
      return render(request,"index.html",{'msg':'Student update Successfully'})

  

  return render(request,"index.html",{'msg':'Student Registered Successfully'})


def display(request):
  students = Student.objects.all()
  return render(request,"display.html",{'students':students})


def delete(request):
  id = request.GET.get('id')
  s = Student.objects.get(pk=id)
  s.delete()
  return redirect('display')


def edit(request):
    id = request.GET.get('id')
    s = Student.objects.get(id=id)

    return render(request, "index.html", {'s': s})