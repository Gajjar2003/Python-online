from django.urls import path
from myappp.views import *


urlpatterns = [

    path('comapny_view',company_view,name='company_view'),
    path('company_add',company_add,name='company_add'),
    path("companybyid/<id>",companybyid,name="companybyid"),
    path("comapny_update/<id>",company_update,name="company_update"),
    path("company_delete/<id>",company_delete,name="company_delete"),


    path('employee_view',employee_view,name='employee_view'),
    path('employee_add',employee_add,name='employee_add'),
    path("employeebyid/<id>",employeebyid,name="employeebyid"),
    path("employee_update/<id>",employee_update,name="employee_update"),
    path("employee_delete/<id>",employee_delete,name="employee_delete"),
]