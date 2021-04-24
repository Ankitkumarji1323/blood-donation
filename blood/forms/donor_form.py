from django import forms
from django.forms import TextInput, Select, Textarea, DateTimeInput, FileInput

from blood.models.donor import Donor, RecentDonor


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'address': Textarea(attrs={'class': 'form-control', 'id': 'address', 'rows': 4}),
            'current_location': Select(attrs={'class': 'form-control', 'id': 'current_location'}),
            'reference_name': TextInput(attrs={'class': 'form-control', 'id': 'reference_name'}),
            'reference_number': TextInput(attrs={'class': 'form-control', 'id': 'reference_number'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'phone_number'}),
            'select_blood': Select(attrs={'class': 'form-control', 'id': 'select_blood'}),
            'email_address': TextInput(attrs={'class': 'form-control', 'id': 'email_address'}),
            'date_of_birth': DateTimeInput(attrs={'class': 'form-control', 'id': 'date_of_birth', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'profession': TextInput(attrs={'class': 'form-control', 'id': 'profession'}),
            'profile_picture': FileInput(attrs={'class': 'form-control', 'id': 'profile_picture'}),
            'last_donation_date': DateTimeInput(
                attrs={'class': 'form-control', 'id': 'last_donation_date', 'type': 'date'}),
        }


class RecentDonorFrom(forms.ModelForm):
    class Meta:
        model = RecentDonor
        fields = '__all__'

        widgets = {
            'patient_name': TextInput(attrs={'class': 'form-control', 'id': 'patient_name'}),
            'patient_number': TextInput(attrs={'class': 'form-control', 'id': 'patient_number'}),
            'address': Textarea(attrs={'class': 'form-control', 'id': 'address', 'rows': 4}),
            'last_donation': DateTimeInput(attrs={'class': 'form-control', 'id': 'last_donation', 'type': 'date'}),
            'donor_name': Select(attrs={'class': 'form-control', 'id': 'donor_name'}),
            'picture': FileInput(attrs={'class': 'form-control', 'id': 'picture'}),
        }
