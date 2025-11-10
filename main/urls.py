from django.urls import path
from . import views  # '.' means 'from this current folder'

# This is the "phone book" for the 'main' app.

urlpatterns = [
    # When someone visits the "root" path (''), 
    # run the 'home' function from views.py.
    # We also give this URL a name='home' so we can find it easily.
    path('', views.home, name='home'),
    
    # URL for the driver login page
    path('login/driver/', views.driver_login, name='driver_login'),
    
    # URL for the guardian login page
    path('login/guardian/', views.guardian_login, name='guardian_login'),
    
    # URL for the driver dashboard
    path('dashboard/driver/', views.driver_dashboard, name='driver_dashboard'),
    
    # URL for the guardian dashboard
    path('dashboard/guardian/', views.guardian_dashboard, name='guardian_dashboard'),
]