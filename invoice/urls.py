from django.urls import path
from .views import home, clients, createClient, products, createInvoice, createInvoiceComplete


urlpatterns = [
    path('', home, name='home'),
    path('clients/', clients, name='clients'),
    path('clients/create/', createClient, name='create_client'),
    path('products/', products, name='products'),
    path('invoices/create/', createInvoice, name='create_invoice'),
    path('invoices/create/<slug:slug>/complete/', createInvoiceComplete, name='create_invoice_complete')
]
