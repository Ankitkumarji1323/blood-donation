from django.urls import path
from blood.views.dashboard_view import Dashboard
from blood.views.homepage_views import Homepage
from blood.views.auth_views import Login, SingUpView, Logout
from blood.views.donor_views import CreateDonorView

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('login/', Login.as_view(), name="login"),
    path('registration/', SingUpView.as_view(), name="registration"),
    path('logout/', Logout.as_view(), name="logout"),
    path('add-donor/', CreateDonorView.as_view(), name="create_donor"),
]
