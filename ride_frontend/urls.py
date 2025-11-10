from django.contrib import admin
from django.urls import path, include  # <-- Make sure 'include' is added

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This is the line that matters.
    # It tells Django to look for URLs in 'main.urls'
    path('', include('main.urls')),
]