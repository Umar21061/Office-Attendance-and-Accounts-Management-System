# Importing necessary modules
from rest_framework import generics
from .models import Employee, Attendance, Accounts
from .serializers import EmployeeSerializer, AttendanceSerializer, AccountsSerializer

# Defining views for Employee CRUD operations
class EmployeeListCreate(generics.ListCreateAPIView):
    # Queryset to retrieve all Employee objects
    queryset = Employee.objects.all()
    # Serializer class for Employee objects
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # Queryset to retrieve all Employee objects
    queryset = Employee.objects.all()
    # Serializer class for Employee objects
    serializer_class = EmployeeSerializer

# Defining views for Attendance CRUD operations
class AttendanceListCreate(generics.ListCreateAPIView):
    # Queryset to retrieve all Attendance objects
    queryset = Attendance.objects.all()
    # Serializer class for Attendance objects
    serializer_class = AttendanceSerializer

class AttendanceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # Queryset to retrieve all Attendance objects
    queryset = Attendance.objects.all()
    # Serializer class for Attendance objects
    serializer_class = AttendanceSerializer

# Defining views for Accounts CRUD operations
class AccountsListCreate(generics.ListCreateAPIView):
    # Queryset to retrieve all Accounts objects
    queryset = Accounts.objects.all()
    # Serializer class for Accounts objects
    serializer_class = AccountsSerializer

class AccountsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # Queryset to retrieve all Accounts objects
    queryset = Accounts.objects.all()
    # Serializer class for Accounts objects
    serializer_class = AccountsSerializer
