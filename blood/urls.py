from django.urls import path
from blood.views.dashboard_view import Dashboard
from blood.views.homepage_views import Homepage
from blood.views.auth_views import Login, SingUpView, Logout
from blood.views.location_views import LocationCreateListView
from blood.views.donor_views import *

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('login/', Login.as_view(), name="login"),
    path('registration/', SingUpView.as_view(), name="registration"),
    path('logout/', Logout.as_view(), name="logout"),
    path('location/', LocationCreateListView.as_view(), name="location"),
    path('add-donor/', CreateDonorView.as_view(), name="create_donor"),
    path('donor-list/', DonorListView.as_view(), name="donor_list"),
    path('donor-detail/<pk>/', DonorDetailView.as_view(), name="donor_detail"),
    path('donor-update/<pk>/', DonorUpdateView.as_view(), name="donor_update"),
    path('donor-delete/<pk>/', DonorDeleteView.as_view(), name="donor_delete"),
    path('filter-blood/', FilterDonor.as_view(), name="filter_blood"),
    path('filter-blood/', FilterDonor.as_view(), name="filter_blood"),
    path('recent-donor/', RecentDonorListView.as_view(), name="recent_donor"),
]
