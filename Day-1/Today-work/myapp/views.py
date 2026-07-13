from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def table(request):
    return render(request,"table.html")

def contact(request):
    return render(request,"contact.html")