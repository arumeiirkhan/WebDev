from django.shortcuts import render
from django.http import JsonResponse
from .models import Company, Vacancy
# Create your views here.

def api_home(request):
    return HttpResponse("Welcome to the hh-back API!")

def companies(request):
    companies = Company.objects.all()
    data = {"companies": list(companies.values())}
    return JsonResponse(data)

def company_id(request, id):
    try:
        company = Company.objects.get(id = id)
        data = { "companies": {
            "name" : company.name,
            "description" : company.description,
            "city" : company.city,
            "address" : company.address
        }}
    except Company.DoesNotExist:
        data = {"error": "Company not found"}
    return JsonResponse(data)

def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
        vacancies = Vacancy.objects.filter(company=company)
        data = {"vacancies": list(vacancies.values())}
    except Company.DoesNotExist:
        data = {"error": "Company not found"}
    return JsonResponse(data)

def vacancies(request):
    vacancies = Vacancy.objects.all()
    data = {"vacancies": list(vacancies.values())}
    return JsonResponse(data)

def vacancy_id(request, id):
    try:
        vacancy = Vacancy.objects.get(id = id)
        data = { "vacancies": {
            "name" : vacancy.name,
            "description" : vacancy.description,
            "salary" : vacancy.salary,
            "company" : vacancy.company
        }}
    except Vacancy.DoesNotExist:
        data = {"error": "Vacancy not found"}
    return JsonResponse(data)

from django.http import JsonResponse
from django.db.models import Count

def top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary').values('name', 'description', 'salary')[:10]
    data = {'vacancies': list(vacancies)}
    return JsonResponse(data, safe=False)
