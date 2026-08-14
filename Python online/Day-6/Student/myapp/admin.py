from django.contrib import admin
from myapp.models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'subject', 'marks')

admin.site.register(Student,StudentAdmin)
