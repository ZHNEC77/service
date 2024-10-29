from django.contrib import admin
from .models import Product, Type, Price

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'barcode', 'updated_at', 'type')
    search_fields = ('name', 'barcode')  # Добавляем поиск по названию и штрихкоду

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('currency', 'amount')

admin.site.register(Product, ProductAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Price, PriceAdmin)