from django.contrib import admin
from myapp.models import *

class StudentDiaply(admin.ModelAdmin):
    list_display = ('name','email','age')
    search_fields = ('name','email','age')



admin.site.register(Student,StudentDiaply)
admin.site.register(Coures)

# Register your models here.
