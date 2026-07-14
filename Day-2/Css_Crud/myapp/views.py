from django.shortcuts import render,redirect
from myapp.models import *

def index(request):
    return render(request,"index.html")

def register(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    qty = request.POST.get('qty')
    price = request.POST.get('price')

    if not id:

        Product.objects.create(name=name,qty=qty,price=price)

        return render(request,"index.html",{'meg':'successfully done !!'})
    else:
          p = Product.objects.get(pk=id)
          p.name= name
          p.qty = qty
          p.price = price
          p.save()
          return render(request,"index.html",{'meg':' update successfully done !!'})

def display(request):
    products = Product.objects.all()
    return render(request,"display.html",{'products':products})

def delete(request):
    id = request.GET.get('id')
    p = Product.objects.get(pk=id)
    p.delete()
    return redirect('display')

def edit(request):
    id = request.GET.get('id')
    p = Product.objects.get(pk=id)
    return render(request,"index.html",{'p':p})