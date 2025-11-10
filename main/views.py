
from django.shortcuts import render

# Create your views here.

def home(request):
    """
    This view function handles the logic for the home page.
    It tells Django to find and render the 'main/home.html' template.
    """
    # We will create the 'main/home.html' file in the next steps.
    return render(request, 'main/home.html')

def driver_login(request):
    """
    This view will handle the driver login page.
    """
    # We'll create 'main/driver_login.html' later
    return render(request, 'main/driver_login.html')

def guardian_login(request):
    """
    This view will handle the guardian login page.
    """
    # We'll create 'main/guardian_login.html' later
    return render(request, 'main/guardian_login.html')

def driver_dashboard(request):
    """
    This view will handle the driver's dashboard.
    """
    # We'll create 'main/driver_dashboard.html' later
    return render(request, 'main/driver_dashboard.html')

def guardian_dashboard(request):
    """
    This view will handle the guardian's dashboard.
    """
    # We'll create 'main/guardian_dashboard.html' later
    return render(request, 'main/guardian_dashboard.html')
