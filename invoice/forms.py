from django import forms
from .models import Client, Invoice, Product


class DateInput(forms.DateInput):
    input_type = 'date'


class ClientCreationForm(forms.ModelForm):
    clientLogo = forms.ImageField()

    class Meta:
        model = Client
        fields = ('name', 'addressLine1', 'postalCode', 'province', 'phoneNumber', 'email', 'clientLogo')
        widgets = {
            "clientLogo": forms.ClearableFileInput(
            ),
        }


class InvoiceCreationForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('number', 'invoiceTitle', 'dueDate', 'paymentStatus', 'client')
        widgets = {
            'dueDate' : DateInput(),
        }



class ProductCreationForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = ('productTitle', 'description', 'quantity', 'price', 'currency', 'image')
        widgets = {
            'description':forms.Textarea(
                attrs={
                    'rows':5,
                }
            )
        }
