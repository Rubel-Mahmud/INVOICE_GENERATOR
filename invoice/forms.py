from django import forms
from .models import Client


class ClientCreationForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'addressLine1', 'postalCode', 'province', 'phoneNumber', 'email')
