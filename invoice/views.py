from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from uuid import uuid4

# html to pdf start import
from django.http import HttpResponse
import pdfkit
from django.template.loader import get_template
from django.conf import settings
import os
# html to pdf end import

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



def clientSearch(request):
    queryset = {}
    if request.method == "POST":
        inputData = request.POST['searchText']
        clients = Client.objects.filter(name__contains=inputData)
        if bool(clients) == False :
            clients = Client.objects.filter(addressLine1__contains=inputData)
        queryset['clients'] = clients
    else:
        clients = Client.objects.all()
        queryset['clients'] = clients
    return render(request, 'invoice/client_search.html', queryset)



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
            invoiceTotal = invoice.invoiceTotal
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
    context = {}
    invoice = Invoice.objects.get(uniqueId=slug)
    context['invoice'] = invoice
    return render(request, 'invoice/html_to_pdf_test.html', context)



# html to pdf View
def createPDF(request):
    #The name of your PDF file
    filename = 'first_invoice_to_ilma.pdf'

    #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('invoice/html_to_pdf_test.html')

    #Add any context variables you need to be dynamically rendered in the HTML
    context = {}
    context['invoice'] = 'invoice'
    # context['name'] = 'Skolo'
    # context['surname'] = 'Online'

    #Render the HTML
    html = template.render(context)

    #Options - Very Important [Don't forget this]
    options = {
        'encoding': 'UTF-8',
        'javascript-delay':'2000', #Optional
        'enable-local-file-access': None, #To be able to access CSS
        'page-size': 'A4',
        'custom-header' : [
            ('Accept-Encoding', 'gzip')
        ],
    }
    #Javascript delay is optional

    #Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    #IF you have CSS to add to template
    css1 = os.path.join(settings.STATIC_ROOT, 'css', 'styles.css')
    css2 = os.path.join(settings.STATIC_ROOT, 'css', 'pdf.css')
    # css2 = os.path.join(settings.STATIC_ROOT, 'css', 'bootstrap.css')

    #Create the file
    file_content = pdfkit.from_string(html, False, configuration=config, options=options)

    #Create the HTTP Response
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename = {}'.format(filename)

    #Return
    return response
