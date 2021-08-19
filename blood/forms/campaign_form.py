from django import forms
from django.forms import TextInput, NumberInput, DateTimeInput, FileInput

from blood.models.campaign import Campaign


class CampaignDonorFrom(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'

        widgets = {
            'campaign_name': TextInput(attrs={'class': 'form-control', 'id': 'campaign_name'}),
            'day_name': TextInput(attrs={'class': 'form-control', 'id': 'day_name'}),
            'sponsor_by': TextInput(attrs={'class': 'form-control', 'id': 'sponsor_by'}),
            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'material_cost': NumberInput(attrs={'class': 'form-control', 'id': 'material_cost'}),
            'other_cost': NumberInput(attrs={'class': 'form-control', 'id': 'other_cost'}),
            'picture': FileInput(attrs={'class': 'form-control', 'id': 'picture'}),
            'campaign_date': DateTimeInput(attrs={'class': 'form-control', 'id': 'campaign_date', 'type': 'date'}),
        }
