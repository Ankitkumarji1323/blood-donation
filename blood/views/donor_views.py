from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from blood.models.donor import Donor
from blood.forms.donor_form import DonorForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateDonorView(CreateView):
    template_name = 'members/add_donor.html'
    model = Donor
    form_class = DonorForm
