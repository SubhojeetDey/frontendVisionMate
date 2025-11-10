from django.urls import path
from . import views  # '.' means 'from this current folder'

# This 'app_name' helps Django find your URLs when you use {% url '...' %} in your templates
app_name = 'main'

urlpatterns = [
    # URL for the home page
    path('', views.home, name='home'),
    
    # URL for the driver login page
    path('login/driver/', views.driver_login, name='driver_login'),
    
    # URL for the guardian login page
    path('login/guardian/', views.guardian_login, name='guardian_login'),
    
    # URL for the driver dashboard
    path('dashboard/driver/', views.driver_dashboard, name='driver_dashboard'),
    
    # URL for the guardian dashboard
    path('dashboard/guardian/', views.guardian_dashboard, name='guardian_dashboard'),
    
    # NEW: URL for logging out
    path('logout/', views.user_logout, name='logout'),
]