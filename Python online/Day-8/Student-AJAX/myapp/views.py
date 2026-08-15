from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import Student


def index(request):
    return render(request, "index.html")


def register(request):

    if request.method == "POST":

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        age = request.POST.get("age")
        subject = request.POST.get("subject")
        marks = request.POST.get("marks")

        Student.objects.create(
            fname=fname,
            lname=lname,
            email=email,
            age=age,
            subject=subject,
            marks=marks
        )

        return HttpResponse("Student added successfully!")


def display(request):

    students = Student.objects.all()

    return JsonResponse({
        "students": list(students.values())
    })


def delete(request):

    sid = request.GET.get("sid")

    student = Student.objects.get(pk=sid)

    student.delete()

    return HttpResponse("Student deleted successfully!")


def edit(request):

    sid = request.GET.get("sid")

    student = Student.objects.filter(pk=sid)

    return JsonResponse({
        "s": list(student.values())
    })


def update(request):

    if request.method == "POST":

        id = request.POST.get("id")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        age = request.POST.get("age")
        subject = request.POST.get("subject")
        marks = request.POST.get("marks")

        student = Student.objects.get(pk=id)

        student.fname = fname
        student.lname = lname
        student.email = email
        student.age = age
        student.subject = subject
        student.marks = marks

        student.save()

        return HttpResponse("Student updated successfully!")

    return HttpResponse("Invalid request!")