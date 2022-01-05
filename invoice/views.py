from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from uuid import uuid4
from .models import Client, Product, Invoice
from .forms import ClientCreationForm, InvoiceCreationForm, ProductCreationForm


def home(request):
    context = {}
    invoices = Invoice.objects.all().order_by('-last_updated')
    context['invoices'] = invoices
    return render(request, 'invoice/home.html', context)


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



def deleteProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    slug = product.invoice.uniqueId
    product.delete()
    return redirect('create_invoice_complete', slug)



def invoices(request):
    context = {}
    invoices = Invoice.objects.all().order_by('-last_updated')
    context['invoices'] = invoices
    return render(request, 'invoice/invoices.html', context)




def invoiceDetails(request, id):
    invoice = get_object_or_404(Invoice, pk=id)
    slug = invoice.uniqueId
    return redirect('create_invoice_complete', slug)



def deleteInvoice(request, id):
    invoice = get_object_or_404(Invoice, pk=id)
    invoice.delete()
    return redirect('invoices')



def createInvoice(request):
    number = 'INV-' + str(uuid4()).split('-')[1]
    inv = Invoice.objects.create(number=number)
    inv.uniqueId = number + 'RI' + str(uuid4()).split('-')[2]
    inv.save()
    slug = inv.uniqueId
    return redirect('create_invoice_complete', slug)


def createInvoiceComplete(request, slug):
    context = {}
    invoiceTotal = 0
    invoice = Invoice.objects.get(uniqueId=slug)
    products = invoice.products.all().order_by('-created_at')
    context['products'] = products

    if request.method == 'POST':
        invform = InvoiceCreationForm(request.POST, instance=invoice)
        prdform = ProductCreationForm(request.POST)

        if 'productSubmitButton' in request.POST and prdform.is_valid():
            product = prdform.save(commit=False)
            product.invoice = invoice
            product.save()
            invoiceTotal += int(product.quantity) * int(product.price)
            invoice.invoiceTotal = invoiceTotal
            invoice.save()
            return redirect('create_invoice_complete', slug)

        if 'invoiceSubmitButton' in request.POST and invform.is_valid():
            invform.save()
            return redirect('create_invoice_complete', slug)

    else:
        invform = InvoiceCreationForm(instance=invoice)
        prdform = ProductCreationForm()
        context['invoice'] = invoice
        context['invform'] = invform
        context['prdform'] =prdform
        return render(request, 'invoice/invoice_create_complete.html', context=context)



def invoiceTemplate(request, slug):
    return render(request, 'invoice/invoice_template.html')
