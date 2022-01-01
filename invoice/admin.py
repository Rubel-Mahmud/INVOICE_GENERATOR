from django.contrib import admin
from .models import Client, Product


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'province')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'price')

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
