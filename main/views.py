from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Drivers').exists():
            return redirect('main:driver_dashboard') # FIXED
        elif request.user.groups.filter(name='Guardians').exists():
            return redirect('main:guardian_dashboard') # FIXED
            
    return render(request, 'main/home.html')

def driver_login(request):
    if request.method == 'POST':
        username = request.POST.get('driver_user_id')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.groups.filter(name='Drivers').exists():
                login(request, user)
                return redirect('main:driver_dashboard') # FIXED
            else:
                messages.error(request, 'This account is not a valid driver account.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'main/driver_login.html')

def guardian_login(request):
    if request.method == 'POST':
        username = request.POST.get('guardian_user_id')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.groups.filter(name='Guardians').exists():
                login(request, user)
                return redirect('main:guardian_dashboard') # FIXED
            else:
                messages.error(request, 'This account is not a valid guardian account.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'main/guardian_login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('main:home') # FIXED

# FIXED: Added 'main:' to login_url
@login_required(login_url='main:driver_login') 
def driver_dashboard(request):
    if not request.user.groups.filter(name='Drivers').exists():
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('main:home') # FIXED

    return render(request, 'main/driver_dashboard.html')

# FIXED: Added 'main:' to login_url
@login_required(login_url='main:guardian_login')
def guardian_dashboard(request):
    if not request.user.groups.filter(name='Guardians').exists():
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('main:home') # FIXED

    return render(request, 'main/guardian_dashboard.html')