from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('clients/create/', views.createClient, name='create_client'),
    path('products/', views.products, name='products'),
    path('products/<int:id>/delete/', views.deleteProduct, name='delete_product'),
    path('invoices/', views.invoices, name='invoices'),
    path('invoices/<int:id>/delete/', views.deleteInvoice, name='delete_invoice'),
    path('invoices/<int:id>/details/', views.invoiceDetails, name='invoice_details'),
    path('invoices/create/', views.createInvoice, name='create_invoice'),
    path('invoices/create/<slug:slug>/complete/', views.createInvoiceComplete, name='create_invoice_complete'),
    path('invoices/view/<slug:slug>/template/', views.invoiceTemplate, name='invoice_template'),
    path('pdf/', views.createPDF, name='pdf'),
    path('clients/search/', views.clientSearch, name='client_search'),
]
