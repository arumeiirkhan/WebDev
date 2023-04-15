from django.contrib import admin
from django.urls import path
from api.views import company_list, vacancy_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', company_list),
    path('companies/<int:id>/vacancies/', vacancy_list),
]
