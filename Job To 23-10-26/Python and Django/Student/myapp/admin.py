from django.contrib import admin
from myapp.models import *

class Studentdetlis(admin.ModelAdmin):
  list_display = ["name","age","email","number"]



admin.site.register(Student,Studentdetlis)
# Register your models here.
