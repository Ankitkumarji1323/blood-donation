from django.urls import path
from blood.views.home_views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name="homepage")
]
