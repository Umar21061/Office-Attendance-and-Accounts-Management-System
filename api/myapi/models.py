# Importing necessary modules
from django.contrib.auth.models import User
from django.db import models

# Defining the Employee model
class Employee(models.Model):
    # Linking each Employee to a User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Unique employee ID
    employee_id = models.CharField(max_length=20)
    # Department where the employee works
    department = models.CharField(max_length=100)

# Defining the Attendance model
class Attendance(models.Model):
    # Linking each Attendance entry to an Employee
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Check-in time for the employee
    check_in = models.DateTimeField()
    # Check-out time for the employee (nullable)
    check_out = models.DateTimeField(null=True, blank=True)
    # Date of the attendance record
    date = models.DateField()

# Defining the Accounts model
class Accounts(models.Model):
    # Linking each Accounts entry to an Employee
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Month of the salary details
    month = models.IntegerField()
    # Year of the salary details
    year = models.IntegerField()
    # Basic salary amount
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    # Allowances amount
    allowances = models.DecimalField(max_digits=10, decimal_places=2)
    # Deductions amount
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
