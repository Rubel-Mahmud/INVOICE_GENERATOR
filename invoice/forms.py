from django import forms
from .models import Client, Invoice, Product


class ClientCreationForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'addressLine1', 'postalCode', 'province', 'phoneNumber', 'email')



class InvoiceCreationForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('number', 'invoiceTitle', 'dueDate', 'paymentStatus', 'client')



class ProductCreationForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Products Description'}),
        max_length=4000
    )

    class Meta:
        model = Product
        fields = ('productTitle', 'description', 'quantity', 'price', 'currency')
