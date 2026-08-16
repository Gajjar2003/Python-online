from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *


# Create your views here.
def index(request):
  return render(request,"index.html")

def regiter(request):
  name = request.POST.get('name')
  qty = request.POST.get('qty')
  price = request.POST.get('price')

  Prdouct.objects.create(name=name,qty=qty,price=price)
  return HttpResponse("Add Product into Tables")


def display(request):
  products = Prdouct.objects.all()
  return JsonResponse({'products': list(products.values())})


def delete(request):
  pid = request.GET.get('pid')
  p = Prdouct.objects.get(pk=pid)
  p.delete()
  return HttpResponse("Product deleted Into Table")


def edit(request):
  pid = request.GET.get('pid')
  p = Prdouct.objects.filter(pk=pid)
  return JsonResponse({'p':list(p.values())})

def update(request):

    id = request.POST.get('id')
    name = request.POST.get('name')
    qty = request.POST.get('qty')
    price = request.POST.get('price')

    p = Prdouct.objects.get(pk=id)

    p.name = name
    p.qty = qty
    p.price = price

    p.save()

    return HttpResponse("Product Updated Successfully")