# Importing necessary modules
from rest_framework import serializers
from .models import Employee, Attendance, Accounts

# Serializer for Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to serialize
        model = Employee
        # Include all fields in the serialization
        fields = '__all__'

# Serializer for Attendance model
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to serialize
        model = Attendance
        # Include all fields in the serialization
        fields = '__all__'

# Serializer for Accounts model
class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to serialize
        model = Accounts
        # Include all fields in the serialization
        fields = '__all__'
