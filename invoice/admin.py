from django.contrib import admin
from .models import Client, Product, Invoice


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'province')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'price')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'paymentStatus')


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Invoice, InvoiceAdmin)
