from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import company_list, vacancy_list

urlpatterns = [
    path('companies/', views.company_list),
    path('companies/<int:id>/vacancies/', views.vacancy_list),
]


urlpatterns = format_suffix_patterns(urlpatterns)