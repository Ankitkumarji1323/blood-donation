from django import forms
from django.forms import TextInput, Select, Textarea, DateTimeInput

from blood.models.donor import Donor


class LocationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'address': Textarea(attrs={'class': 'form-control', 'id': 'address'}),
            'current_location': Select(attrs={'class': 'form-control', 'id': 'current_location'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'phone_number'}),
            'email_address': TextInput(attrs={'class': 'form-control', 'id': 'email_address'}),
            'date_of_birth': DateTimeInput(attrs={'class': 'form-control', 'id': 'date_of_birth'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'profession': TextInput(attrs={'class': 'form-control', 'id': 'profession'}),
            'last_donation_date': DateTimeInput(attrs={'class': 'form-control', 'id': 'last_donation_date'}),
        }
