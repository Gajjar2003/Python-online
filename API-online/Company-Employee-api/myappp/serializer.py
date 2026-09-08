from rest_framework import serializers
from myappp.models import *

class Companyserializer(serializers.ModelSerializer):
      class Meta:
            model =Company
            fields = '__all__'


class Employeeserializer(serializers.ModelSerializer):
      class Meta:
            model =Employee
            fields = '__all__'
      