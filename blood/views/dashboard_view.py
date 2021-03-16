from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from blood.models.donor import Donor


class Dashboard(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Dashboard, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['donor_list'] = Donor.objects.all()
        return context

    template_name = 'dashboard/dashboard.html'
