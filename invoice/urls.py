from django.urls import path
from .views import home, clients, createClient, products


urlpatterns = [
    path('', home, name='home'),
    path('clients/', clients, name='clients'),
    path('clients/create/', createClient, name='create_client'),
    path('products/', products, name='products'),
    # path('products/create/', createProduct, name='create_product'),
]
