"""shopback URL Configuration

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
from django.urls import path, include
from api.views import product_list, product_detail, category_list, category_detail, category_products
from django.contrib import admin

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:id>/', category_detail, name='category_detail'),
    path('categories/<int:id>/products/', category_products, name='category_products'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]


