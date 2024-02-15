from rest_framework import generics  # Importing generics from rest_framework module
from rest_framework.permissions import IsAuthenticated  # Importing IsAuthenticated permission class

from .models import Employee, Attendance, Accounts  # Importing models from current package
from .serializers import (  # Importing serializers from current package
    EmployeeSerializer, AttendanceSerializer, AccountsSerializer,
    TokenObtainPairSerializer, TokenRefreshSerializer
)

# Views for JWT token
class TokenObtainPairView(generics.CreateAPIView):
    serializer_class = TokenObtainPairSerializer  # Serializer class for obtaining token
    permission_classes = (IsAuthenticated,)  # Authentication required for this view

class TokenRefreshView(generics.CreateAPIView):
    serializer_class = TokenRefreshSerializer  # Serializer class for refreshing token
    permission_classes = (IsAuthenticated,)  # Authentication required for this view

# Defining views for Employee CRUD operations
class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()  # Queryset for Employee model
    serializer_class = EmployeeSerializer  # Serializer class for Employee model
    permission_classes = (IsAuthenticated,)  # Authentication required for this view

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()  # Queryset for Employee model
    serializer_class = EmployeeSerializer  # Serializer class for Employee model
    permission_classes = (IsAuthenticated,)  # Authentication required for this view

# Defining views for Attendance CRUD operations
class AttendanceListCreate(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()  # Queryset for Attendance model
    serializer_class = AttendanceSerializer  # Serializer class for Attendance model
    permission_classes = (IsAuthenticated,)  # Authentication required for this view

class AttendanceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()  # Queryset for Attendance model
    serializer_class = AttendanceSerializer  # Serializer class for Attendance model
    permission_classes = (IsAuthenticated,)  # Authentication required for this view

# Defining views for Accounts CRUD operations
class AccountsListCreate(generics.ListCreateAPIView):
    queryset = Accounts.objects.all()  # Queryset for Accounts model
    serializer_class = AccountsSerializer  # Serializer class for Accounts model
    permission_classes = (IsAuthenticated,)  # Authentication required for this view

class AccountsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accounts.objects.all()  # Queryset for Accounts model
    serializer_class = AccountsSerializer  # Serializer class for Accounts model
    permission_classes = (IsAuthenticated,)  # Authentication required for this view
