from django.contrib import admin
from .models import DriverProfile, Passenger, Ride

# --- DriverProfile Admin ---
class DriverProfileAdmin(admin.ModelAdmin):
    """
    Customizes how the DriverProfile is shown in the admin.
    """
    list_display = ('user', 'status', 'mobile_no', 'vehicle_number')
    search_fields = ('user__username', 'vehicle_number')
    list_filter = ('status',)

# --- Passenger Admin ---
class PassengerAdmin(admin.ModelAdmin):
    """
    Customizes how the Passenger is shown in the admin.
    Shows the auto-generated device_key.
    """
    list_display = ('name', 'guardian', 'mobile_no', 'device_key_short')
    search_fields = ('name', 'guardian__username')
    readonly_fields = ('device_key',) # Make the key read-only

    def device_key_short(self, obj):
        # Shows just the first 8 chars of the key in the list
        return str(obj.device_key).split('-')[0]
    device_key_short.short_description = 'Device Key'

# --- Ride Admin ---
class RideAdmin(admin.ModelAdmin):
    """
    Customizes how the Ride is shown in the admin.
    """
    list_display = ('id', 'passenger', 'driver_name', 'status', 'created_at')
    search_fields = ('passenger__name', 'assigned_driver__user__username')
    list_filter = ('status',)
    readonly_fields = ('created_at',)

    def driver_name(self, obj):
        if obj.assigned_driver:
            return obj.assigned_driver.user.username
        return "N/A"
    driver_name.short_description = 'Driver'

# --- Register your models ---
admin.site.register(DriverProfile, DriverProfileAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Ride, RideAdmin)

# Register your models here.
