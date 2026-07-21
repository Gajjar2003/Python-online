from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    name = request.POST.get('name')
    qty = request.POST.get('qty')
    price = request.POST.get('price')

    Product.objects.create(name=name,qty=qty,price=price)
    return HttpResponse("Product Add Success !!")

def display(request):
    p = Product.objects.all()
    return JsonResponse({'p':list(p.values())})

def delete(request):
    pid = request.GET.get('pid')
    p = Product.objects.get(pk=pid)
    p.delete()
    return HttpResponse("Products Delete Into a Tables")

def edit(request):
    pid = request.GET.get('pid')
    p = Product.objects.filter(pk=pid)
    return JsonResponse({'p':list(p.values())})

def update(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    qty = request.POST.get('qty')
    price = request.POST.get('price')

    p = Product.objects.get(pk=id)

    p.name = name
    p.qty = qty
    p.price = price
    p.save()

    return HttpResponse("Product Updated Successfully !!")