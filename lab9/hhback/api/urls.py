"""hhback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import api_home, companies, company_id, company_vacancies, vacancies, vacancy_id, top_ten


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_home, name = 'api_home'),
    path('companies/', companies, name = 'companies'),
    path('companies/<int:id>/', company_id, name = 'company_id'),
    path('companies/<int:id>/vacancies/', company_vacancies, name = 'company_vacancies'),
    path('vacancies/', vacancies, name = 'vacancies'),
    path('vacancies/<int:id>/', vacancy_id, name = 'vacancy_id'),
    path('vacancies/top_ten', top_ten, name = 'top_ten')
]
