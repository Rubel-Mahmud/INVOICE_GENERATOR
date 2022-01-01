from django.shortcuts import render
from django.shortcuts import redirect
from .models import Client, Product, Invoice
from .forms import ClientCreationForm


def home(request):
    return render(request, 'invoice/home.html')


def clients(request):
    context = {}
    clients = Client.objects.all().order_by('-created_at')
    context['clients'] = clients
    return render(request, 'invoice/clients.html', context=context)


def createClient(request):
    context = {}
    if request.method == "POST":
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientCreationForm()
        context['form'] = form
    return render(request, 'invoice/create_client.html', context=context)



def products(request):
    context = {}
    products = Product.objects.all().order_by('-created_at')
    context['products'] = products
    return render(request, 'invoice/products.html', context=context)

