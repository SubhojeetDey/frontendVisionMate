from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import DriverProfile, Passenger

# --- Helper function to check group membership ---
def is_in_group(user, group_name):
    """
    Checks if a user is in a specific group.
    """
    return user.groups.filter(name=group_name).exists()

# --- Public Pages ---

def home(request):
    """
    Renders the main home page.
    """
    return render(request, 'main/home.html')

# --- Authentication Pages ---

def driver_login(request):
    """
    Handles the login form for Drivers.
    """
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('driver_user_id')
        password = request.POST.get('password')

        # 1. Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 2. Check if they are in the 'Drivers' group
            if is_in_group(user, 'Drivers'):
                login(request, user)
                return redirect('main:driver_dashboard')
            else:
                messages.error(request, 'This account is not a valid driver account.')
        else:
            messages.error(request, 'Invalid username or password.')
            
    # CORRECTED PATH: Removed 'main/templates/'
    return render(request, 'main/driver_login.html')


def guardian_login(request):
    """
    Handles the login form for Guardians.
    """
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('guardian_user_id')
        password = request.POST.get('password')

        # 1. Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 2. Check if they are in the 'Guardians' group
            if is_in_group(user, 'Guardians'):
                login(request, user)
                return redirect('main:guardian_dashboard')
            else:
                messages.error(request, 'This account is not a valid guardian account.')
        else:
            messages.error(request, 'Invalid username or password.')

    # CORRECTED PATH: Removed 'main/templates/'
    return render(request, 'main/guardian_login.html')


def user_logout(request):
    """
    Logs out any user and redirects to the home page.
    """
    logout(request)
    return redirect('main:home')


# --- Protected Dashboard Pages ---

@login_required(login_url='main:driver_login')
def driver_dashboard(request):
    """
    Displays the dashboard for the logged-in driver.
    Ensures the user is a Driver.
    """
    # Redirect if a Guardian somehow gets here
    if not is_in_group(request.user, 'Drivers'):
        return redirect('main:home')

    # --- Get Dynamic Data ---
    # Fetch the driver's profile to show their status
    try:
        driver_profile = request.user.driver_profile
    except DriverProfile.DoesNotExist:
        # This is a fallback in case the profile wasn't created in the admin
        driver_profile = None

    context = {
        'driver_profile': driver_profile
    }
    # CORRECTED PATH: Removed 'main/templates/'
    return render(request, 'main/driver_dashboard.html', context)


@login_required(login_url='main:guardian_login')
def guardian_dashboard(request):
    """
    Displays the dashboard for the logged-in guardian.
    Ensures the user is a Guardian.
    """
    # Redirect if a Driver somehow gets here
    if not is_in_group(request.user, 'Guardians'):
        return redirect('main:home')

    # --- Get Dynamic Data ---
    # Fetch the passengers (e.g., "Priya Sharma") that this guardian is responsible for
    # We use .first() to get the first passenger for this demo
    passenger = Passenger.objects.filter(guardian=request.user).first()

    context = {
        'passenger': passenger
    }
    # CORRECTED PATH: Removed 'main/templates/'
    return render(request, 'main/guardian_dashboard.html', context)