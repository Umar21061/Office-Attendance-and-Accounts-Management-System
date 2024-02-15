from django.urls import path  # Importing path function from django.urls module

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView  # Importing views from rest_framework_simplejwt module

from .views import (  # Importing views from current package
    EmployeeListCreate, EmployeeRetrieveUpdateDestroy,  # Importing Employee views
    AttendanceListCreate, AttendanceRetrieveUpdateDestroy,  # Importing Attendance views
    AccountsListCreate, AccountsRetrieveUpdateDestroy  # Importing Accounts views
)

urlpatterns = [  # Defining URL patterns list

    # URL pattern for Employee list and creation
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),

    # URL pattern for Employee detail, update, and deletion
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-detail'),

    # URL pattern for Attendance list and creation
    path('attendances/', AttendanceListCreate.as_view(), name='attendance-list-create'),

    # URL pattern for Attendance detail, update, and deletion
    path('attendances/<int:pk>/', AttendanceRetrieveUpdateDestroy.as_view(), name='attendance-detail'),

    # URL pattern for Accounts list and creation
    path('accounts/', AccountsListCreate.as_view(), name='accounts-list-create'),

    # URL pattern for Accounts detail, update, and deletion
    path('accounts/<int:pk>/', AccountsRetrieveUpdateDestroy.as_view(), name='accounts-detail'),

    # URL pattern for token obtain (login)
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # URL pattern for token refresh
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # URL pattern for token verification
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]
