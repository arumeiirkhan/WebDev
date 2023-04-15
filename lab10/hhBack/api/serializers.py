from api.models import Company
from rest_framework import serializers
from .models import *  

class CompanySerializer1(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__' #('id', 'name')

class VacancySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'