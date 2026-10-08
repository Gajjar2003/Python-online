from django.contrib import admin
from myapp.models import *


class Employeedetalis(admin.ModelAdmin):
  list_display=('name','age','email','number','city')


admin.site.register(Employee,Employeedetalis)

# Register your models here.
