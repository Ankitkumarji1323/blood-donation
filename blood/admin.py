from django.contrib import admin

from blood.models.location import Location
from blood.models.donor import Donor, RecentDonor
from blood.models.preferences import ApplicationSetting
from blood.models.campaign import Campaign


class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'is_active']
    search_fields = ['name', 'parent']


admin.site.register(Location, LocationAdmin)


class DonorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone_number', 'select_blood', 'last_donation_date', 'gender']
    search_fields = ['first_name', 'phone_number', 'select_blood', 'last_donation_date']
    edit_fields = ['phone_number', 'select_blood']
    link_display = ['id', 'first_name']


admin.site.register(Donor, DonorAdmin)

admin.site.register(ApplicationSetting)


class RecentDonorAdmin(admin.ModelAdmin):
    list_display = ['id', 'donor_name', 'last_donation', 'patient_name', 'address', 'patient_number']
    search_fields = ['id', 'donor_name', 'patient_name']
    list_display_links = ['id', 'donor_name', 'last_donation']


admin.site.register(RecentDonor, RecentDonorAdmin)


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['id', 'campaign_name', 'day_name', 'sponsor_by', 'address', 'material_cost', 'other_cost',
                    'campaign_date']
    search_fields = ['campaign_name', 'day_name', 'sponsor_by']
    list_editable = ['day_name', 'material_cost', 'other_cost']
    list_display_links = ['id', 'campaign_name', 'address']


admin.site.register(Campaign, CampaignAdmin)
