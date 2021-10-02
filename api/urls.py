from django.urls import path
from .donor_views import DonorAPIView

urlpatterns = [
    path('donor/', DonorAPIView.as_view()),
]
