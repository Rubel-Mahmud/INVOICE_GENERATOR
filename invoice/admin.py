from django.contrib import admin
from .models import Client, Product, Invoice, Company


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'province')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('productTitle', 'quantity', 'price')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('number', 'invoiceTitle', 'paymentStatus')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'province')


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Company, CompanyAdmin)
