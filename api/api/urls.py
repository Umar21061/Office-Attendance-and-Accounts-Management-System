# api/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapi.urls')),
    # Add a catch-all pattern to redirect /api/ to /api/employees/ or any other default endpoint
    path('api/', RedirectView.as_view(url='employees/', permanent=True)),
]