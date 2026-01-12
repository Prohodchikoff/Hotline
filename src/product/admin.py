from django.contrib import admin
from .models import Product, ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'price',
        'origin_country',
        'create_date',
        'stock',
        'category_id'
    ]


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['path', 'product__product_id']
