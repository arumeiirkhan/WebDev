from django.http import JsonResponse
from api.models import Company, Vacancy
from api.serializers import CompanySerializer2, VacancySerializer2, CompanySerializer1
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer1(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def vacancy_list(request, id):
    company = Company.objects.get(id=id)
    vacancies = Vacancy.objects.filter(company=company)
    serializer = VacancySerializer2(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False) 
