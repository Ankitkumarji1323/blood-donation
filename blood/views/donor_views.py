from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from blood.models.donor import Donor
from blood.forms.donor_form import DonorForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateDonorView(SuccessMessageMixin, CreateView):
    template_name = 'members/add_donor.html'
    model = Donor
    form_class = DonorForm
    success_url = '/add-donor/'
    success_message = "Service has been successfully created!"
