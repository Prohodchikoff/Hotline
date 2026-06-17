from django.contrib import admin
from .models import Attribute, AttributeValue, ProductAttribute


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1


@admin.register(Attribute)
class AttributesAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    search_fields = ['name', 'category__name']
    list_filter = ['category']
    inlines = [AttributeValueInline]


@admin.register(AttributeValue)
class AttributeValuesAdmin(admin.ModelAdmin):
    list_display = ['value', 'attribute']
    search_fields = ['value', 'attribute__name']


@admin.register(ProductAttribute)
class ProductAttributesAdmin(admin.ModelAdmin):
    list_display = ['product', 'attribute', 'value']
    search_fields = ['product__name', 'attribute__name', 'value__value']
    list_filter = ['attribute', 'attribute__category']
    autocomplete_fields = ['product', 'attribute', 'value']
