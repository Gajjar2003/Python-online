from rest_framework import serializers
from empapp.models import *


class deptserializer(serializers.ModelSerializer):
    class Meta:
        model = dept
        fields = '__all__'

class empserializer(serializers.ModelSerializer):
    class Meta:
        model = emp
        fields = '__all__'