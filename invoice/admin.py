from django.contrib import admin
from .models import Client, Product, Invoice


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'province')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('productTitle', 'quantity', 'price')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('number', 'invoiceTitle', 'paymentStatus')


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Invoice, InvoiceAdmin)
