# Import necessary modules
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# Define URL patterns
urlpatterns = [
    # Admin URL pattern
    path('admin/', admin.site.urls),
    # Include API endpoints from the 'myapi' app
    path('api/', include('myapi.urls')),
    # Redirect /api/ to /api/employees/ or any other default endpoint
    path('api/', RedirectView.as_view(url='employees/', permanent=True)),
]
