from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from uuid import uuid4

# Email sending
from django.core.mail import BadHeaderError, EmailMessage

# html to pdf start import
from django.http import HttpResponse
import pdfkit
from django.template.loader import get_template
from django.conf import settings
import os
# html to pdf end import

from .models import Client, Product, Invoice, Company
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
        form = ClientCreationForm(request.POST, request.FILES)
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
        if bool(clients) == False :
            clients = Client.objects.filter(postalCode__contains=inputData)
        if bool(clients) == False :
            clients = Client.objects.filter(phoneNumber__contains=inputData)
        if bool(clients) == False :
            clients = Client.objects.filter(email__contains=inputData)
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
        prdform = ProductCreationForm(request.POST, request.FILES)

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
    company = Company.objects.get(name='IR Soft')
    products = Product.objects.filter(invoice=invoice)
    context['invoice'] = invoice
    context['company'] = company
    context['products'] = products
    return render(request, 'invoice/html_to_pdf_test.html', context)



# html to pdf View
def createPDF(request, slug):

    invoice = Invoice.objects.get(uniqueId = slug)
    company = Company.objects.get(name='IR Soft')
    products = Product.objects.filter(invoice=invoice)

    #The name of your PDF file
    filename = '{}.pdf'.format(invoice.uniqueId)

    #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('invoice/html_to_pdf_test.html')

    #Add any context variables you need to be dynamically rendered in the HTML
    context = {}
    context['invoice'] = invoice
    context['company'] = company
    context['products'] = products

    #Render the HTML
    html = template.render(context)

    #Options - Very Important [Don't forget this]
    options = {
        'encoding': 'UTF-8',
        'javascript-delay':'10', #Optional
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

    #Create the file
    # file_content = pdfkit.from_string(html, False, configuration=config, options=options)

    #Saving the File
    filepath = os.path.join(settings.MEDIA_ROOT, 'client_invoices/')
    os.makedirs(filepath, exist_ok=True)
    pdf_save_path = filepath + filename


    #Save the PDF
    file_content = pdfkit.from_string(html, False, configuration=config, options=options)


    #Create the HTTP Response
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename = {}'.format(filename)

    #Return
    return response



def formTest(request):
    context = {}
    if 'paid' in request.POST:
        message = 'Got paid invoices!'
        context['message'] = message
    elif 'unpaid' in request.POST:
        message = 'Got unpaid invoices!'
        context['message'] = message
    else:
        message = "Found all invoices by default."
        context['message'] = message
    return render(request, 'invoice/test_form_submit.html', context)





def send_email(request, slug):
    pdf_invoice = Invoice.objects.get(uniqueId = slug)
    subject = 'Email Subject'
    message = 'Email messages here..'
    from_email = 'pythondevelopmenttest@gmail.com'
    to_email = pdf_invoice.client.email
    bcc_email = ['pythondevelopmenttest@gmail.com']
    if subject and message and to_email:
        try:
            message = EmailMessage(subject, message, from_email, [to_email], bcc_email)
            message.attach_file('media/client_invoices/{}.pdf'.format(pdf_invoice.uniqueId))
            message.send() #Check here that message.send() is returned 1 or 0
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Email send successfully!')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')




