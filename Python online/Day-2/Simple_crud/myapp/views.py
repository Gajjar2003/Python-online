from django.shortcuts import render,redirect
from Simple_crud.myapp.models import *

def index(request):
    return render(request,"index.html")

def register(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')

    if not id:

        Student.objects.create(name=name,email=email,age=age)
        return render(request,"index.html",{'meg':'Register Successfully Done !!!!!'})
    else : 
        st = Student.objects.get(pk=id)
        st.name = name
        st.email =email
        st.age =age
        st.save()
        return render(request,"index.html",{'meg':'update Successfully Done !!!!!'})


def display(request):
    students = Student.objects.all()
    return render(request,"display.html",{'students':students})


def delete(request):
    id = request.GET.get('id')
    st = Student.objects.get(pk=id)
    st.delete()
    return redirect('display')


def edit(request):
    id = request.GET.get('id')
    st = Student.objects.get(pk=id)
    return render(request,"index.html",{'st':st})
