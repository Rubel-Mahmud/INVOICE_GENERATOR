from django.shortcuts import render
from django.shortcuts import redirect
from uuid import uuid4
from .models import Client, Product, Invoice
from .forms import ClientCreationForm, InvoiceCreationForm, ProductCreationForm


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



def createInvoice(request):
    number = 'INV-' + str(uuid4()).split('-')[1]
    inv = Invoice.objects.create(number=number)
    inv.uniqueId = number + 'RI' + str(uuid4()).split('-')[2]
    inv.save()
    slug = inv.uniqueId
    return redirect('create_invoice_complete', slug)


def createInvoiceComplete(request, slug):
    context = {}
    invoice = Invoice.objects.get(uniqueId=slug)

    if request.method == 'POST':
        invform = InvoiceCreationForm(request.POST, instance=invoice)
        prdform = ProductCreationForm(request.POST)

        if prdform.is_valid():
            product = prdform.save()
            return redirect('create_invoice_complete', slug)

        if invform.is_valid():
            invoice = invform.save(commit=False)
            invoice.product = product
            invoice.save()
            return redirect('create_invoice_complete', slug)

    else:
        invform = InvoiceCreationForm(instance=invoice)
        prdform = ProductCreationForm()
        context['invform'] = invform
        context['prdform'] =prdform
        return render(request, 'invoice/invoice_create_complete.html', context=context)
