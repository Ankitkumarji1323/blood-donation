from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from blood.models.donor import Donor, RecentDonor
from blood.forms.donor_form import DonorForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateDonorView(SuccessMessageMixin, CreateView):
    template_name = 'members/add_donor.html'
    model = Donor
    form_class = DonorForm
    success_url = '/add-donor/'
    success_message = "Member has been successfully created!"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DonorListView(ListView):
    template_name = 'members/donor_list.html'
    model = Donor
    context_object_name = 'donors'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DonorDetailView(DetailView):
    model = Donor
    template_name = 'members/donor_detail.html'
    context_object_name = 'donor'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DonorUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'members/add_donor.html'
    model = Donor
    form_class = DonorForm
    success_url = '/donor-list/'
    success_message = "Member has been successfully updated!"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DonorDeleteView(DeleteView):
    model = Donor
    success_url = '/donor-list/'
    template_name = 'members/donor_confirm_delete.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FilterDonor(ListView):
    template_name = 'filter/filter.html'
    model = Donor


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RecentDonorListView(ListView):
    template_name = 'donor/donor_history.html'
    model = RecentDonor
