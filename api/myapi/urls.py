# Importing necessary modules
from django.urls import path
from .views import (
    EmployeeListCreate, EmployeeRetrieveUpdateDestroy,
    AttendanceListCreate, AttendanceRetrieveUpdateDestroy,
    AccountsListCreate, AccountsRetrieveUpdateDestroy
)

# URL patterns for API endpoints
urlpatterns = [
    # URL pattern for creating and listing employees
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    # URL pattern for retrieving, updating, and deleting employees by their primary key
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-detail'),
    # URL pattern for creating and listing attendances
    path('attendances/', AttendanceListCreate.as_view(), name='attendance-list-create'),
    # URL pattern for retrieving, updating, and deleting attendances by their primary key
    path('attendances/<int:pk>/', AttendanceRetrieveUpdateDestroy.as_view(), name='attendance-detail'),
    # URL pattern for creating and listing accounts
    path('accounts/', AccountsListCreate.as_view(), name='accounts-list-create'),
    # URL pattern for retrieving, updating, and deleting accounts by their primary key
    path('accounts/<int:pk>/', AccountsRetrieveUpdateDestroy.as_view(), name='accounts-detail'),
]
