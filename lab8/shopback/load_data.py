import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopback.settings')
import django
django.setup()
from api.models import Product, Category

with open('testdata.json', 'r') as f:
    data = json.load(f)
    for category_data in data['categories']:
        category = Category.objects.create(
            name=category_data['name']
        )
        for product_data in category_data['products']:
            Product.objects.create(
                name=product_data['name'],
                price=product_data['price'],
                description=product_data['description'],
                count=product_data['count'],
                is_active=product_data['is_active'],
                category=category
            )

print('Data loaded successfully.')
