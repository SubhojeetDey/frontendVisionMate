from django.db import models
from django.contrib.auth.models import User
import uuid 

# --- 1. Driver Profile Model ---
class DriverProfile(models.Model):
    """
    Extends the built-in Django User model for Driver-specific data.
    Driver/Guardian needs this to handle login and dashboards.
    """
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('offline', 'Offline'),
        ('on_ride', 'On Ride'),
    ]
    
    # Links to the Django User (for login)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_profile')
    
    # Renamed to match FastAPI's 'mobile_no'
    mobile_no = models.CharField(max_length=15) 
    vehicle_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    
    # Status used by our dashboard and FastAPI
    status = models.CharField(max_length=10, choices=AVAILABILITY_CHOICES, default='offline')
    
    # Driver's current location (optional)
    current_latitude = models.FloatField(null=True, blank=True)
    current_longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Driver: {self.user.username} ({self.status})"

# --- 2. Passenger Model (The Blind User) ---
class Passenger(models.Model):
    """
    Represents the blind user who presses the IoT button.
    """
    # Links to the Guardian (who is a Django User)
    guardian = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guarded_passengers')
    
    # Renamed fields to match FastAPI schemas
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    adress = models.CharField(max_length=255) # Matches FastAPI spelling 'adress'

    # The unique key for the IoT device to authenticate with FastAPI
    device_key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    # Passenger's last known location
    last_latitude = models.FloatField(null=True, blank=True)
    last_longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Passenger: {self.name}"


# --- 3. Ride Model (Simplified to match FastAPI's ride_request) ---
class Ride(models.Model):
    """
    Represents a single ride request.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('traveling', 'Traveling'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    # Links
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='rides')
    assigned_driver = models.ForeignKey(DriverProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='driven_rides')
    
    # --- Fields required by FastAPI's 'ride_request' schema: ---
    # The actual physical location (FastAPI needs this)
    location = models.CharField(max_length=255) # Renamed to match FastAPI's 'location'
    
    # The user details at the time of the request (redundant, but matches FastAPI schema for request logging)
    user_id = models.CharField(max_length=50) 
    name = models.CharField(max_length=100) 
    phone_no = models.CharField(max_length=15)
    adress = models.CharField(max_length=255)
    
    # Status and Timestamps
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Ride for {self.name} ({self.status})"

# Create your models here.
