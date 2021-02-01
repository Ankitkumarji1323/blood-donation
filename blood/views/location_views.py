from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin


from blood.models.location import Location
from blood.forms.location_form import LocationForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class LocationCreateListView(SuccessMessageMixin, CreateView, ListView):
    template_name = 'location/location.html'
    model = Location
    form_class = LocationForm
    paginate_by = 6
    context_object_name = 'locations'
    success_url = '/location/'
    success_message = "Location successfully created!"

    def get_context_data(self, **kwargs):
        return dict(
            super(LocationCreateListView, self).get_context_data(**kwargs),
            category=self.model.objects.all().order_by('-id')
        )

