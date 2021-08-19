from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from blood.models.campaign import Campaign
from blood.forms.campaign_form import CampaignFrom


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CampaignListView(ListView):
    model = Campaign
    template_name = 'campaign/campaign-list.html'
    context_object_name = 'campaign'


class CampaignCreateView(SuccessMessageMixin, CreateView):
    model = Campaign
    form_class = CampaignFrom
    template_name = 'campaign/add_new_campaign.html'
    success_url = '/campaign/'
    success_message = "Campaign has been successfully created!"
