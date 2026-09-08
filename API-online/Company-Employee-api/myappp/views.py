from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myappp.models import *
from myappp.serializer import *


@api_view(['GET'])
def company_view(request):
    company = Company.objects.all()
    ser = Companyserializer(company, many=True)
    return Response({"data": ser.data})

@api_view(['POST'])
def company_add(request):
    sdata = request.data
    ser = Companyserializer(data=sdata)
    if not ser.is_valid():
        return Response({'error':ser.errors,"meg":"something went wrong"})
    else:
      ser.save()
      return Response({'meg':'Company added successfully'})


@api_view(['GET'])
def companybyid(request,id):
    company = Company.objects.get(pk=id)
    ser = Companyserializer(company)
    return Response({"data": ser.data})

@api_view(['PUT'])
def company_update(request,id):
    sdata = request.data
    cdata = Company.objects.get(pk=id)
    ser = Companyserializer(cdata,sdata)
    if not ser.is_valid():
        return Response({'error':ser.errors})
    else:
      ser.save()
      return Response({"data":ser.data,'meg':'Company updated successfully'}) 

@api_view(['DELETE'])
def company_delete(request,id):
    company = Company.objects.get(pk=id)
    company.delete()
    return Response({'meg':'Company deleted successfully'})



@api_view(['GET'])
def employee_view(request):
    employee = Employee.objects.all()
    ser = Employeeserializer(employee, many=True)
    return Response({"data": ser.data})

@api_view(['POST'])
def employee_add(request):
    sdata = request.data
    ser = Employeeserializer(data=sdata)
    if not ser.is_valid():
        return Response({'error':ser.errors,"meg":"something went wrong"})
    else:
      ser.save()
      return Response({'meg':'Employee added successfully'})

@api_view(['GET'])
def employeebyid(request,id):
    employee = Employee.objects.get(pk=id)
    ser = Employeeserializer(employee)
    return Response({"data": ser.data})

@api_view(['PUT'])
def employee_update(request,id):
    sdata = request.data
    edata = Employee.objects.get(pk=id)
    ser = Employeeserializer(edata,sdata)
    if not ser.is_valid():
        return Response({'error':ser.errors})
    else:
      ser.save()
      return Response({"data":ser.data,'meg':'Employee updated successfully'})

@api_view(['DELETE'])
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return Response({'meg':'Employee deleted successfully'})