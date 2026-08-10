from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from empapp.models import * 
from empapp.serializer import *


class deptApi(APIView):

    def get(self,request):
        depts = dept.objects.all()
        ser = deptserializer(depts,many=True)
        return Response({'data':ser.data})

    def post(self,request):
        ser  = deptserializer(data=request.data)
        if not ser.is_valid():
            return Response({'error':ser.errors})
        else:
            ser.save()
            return Response({'data':ser.data});


class deptupdate(APIView):
    def get(self,request,id):
        depts = dept.objects.get(pk=id)
        ser = deptserializer(depts)
        return Response({'data':ser.data})

    def delete(self,request,id):
        depts = dept.objects.get(pk=id)
        depts.delete()
        return Response({'data':'deleted'})

    def put(self,request,id):
        depts = dept.objects.get(pk=id)
        ser = deptserializer(depts,request.data)
        if not ser.is_valid():
            return Response({'error':ser.errors})
        else:
            ser.save()
            return Response({'data':ser.data});


