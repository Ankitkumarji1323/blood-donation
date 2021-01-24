from django.urls import path
from blood.views.dashboard_view import Dashboard
from blood.views.homepage_views import Homepage

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
]
