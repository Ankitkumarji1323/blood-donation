from django.urls import path
from blood.views.dashboard_view import Dashboard
from blood.views.homepage_views import Homepage
from blood.views.auth_views import LoginView, RegistrationView

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('login/', LoginView.as_view(), name="login"),
    path('registration/', RegistrationView.as_view(), name="registration"),
]
