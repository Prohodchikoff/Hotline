from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'price',
        'origin_country',
        'image',
        'create_date',
        'stock',
    ]
