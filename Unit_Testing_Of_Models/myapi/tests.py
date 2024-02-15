# Importing necessary modules
from django.test import TestCase  
from django.contrib.auth.models import User  
from .models import Employee, Attendance, Accounts  
from datetime import datetime, date  

# Defining a test case class inheriting from Django's TestCase
class ModelsTestCase(TestCase):  
    
# Overriding the setUp method to set up test data before each test method
    def setUp(self): 
         
        
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create a test employee
        self.employee = Employee.objects.create(user=self.user, employee_id='EMP001', department='IT')

        # Create a test attendance record
        self.attendance = Attendance.objects.create(employee=self.employee, check_in=datetime.now(), date=date.today())

        # Create a test accounts record
        self.accounts = Accounts.objects.create(employee=self.employee, month=1, year=2024, basic_salary=5000.00, allowances=1000.00, deductions=500.00)
# Defining a test method for employee creation
    def test_employee_creation(self): 
         
       # Checking if employee_id is set correctly 
        self.assertEqual(self.employee.employee_id, 'EMP001')  
        
# Checking if department is set correctly
        self.assertEqual(self.employee.department, 'IT')  
        
# Defining a test method for attendance creation
    def test_attendance_creation(self): 
         
        # Checking if employee is linked correctly
        self.assertEqual(self.attendance.employee, self.employee) 
         
        # Checking if check_in time is not None
        self.assertIsNotNone(self.attendance.check_in) 
         
        # Checking if date is set correctly
        self.assertEqual(self.attendance.date, date.today()) 
         
# Defining a test method for accounts creation
    def test_accounts_creation(self):
          
        # Checking if employee is linked correctly
        self.assertEqual(self.accounts.employee, self.employee) 
         
         # Checking if month is set correctly
        self.assertEqual(self.accounts.month, 1)
         
        # Checking if year is set correctly
        self.assertEqual(self.accounts.year, 2024) 
         
        # Checking if basic_salary is set correctly
        self.assertEqual(self.accounts.basic_salary, 5000.00)
          
        # Checking if allowances are set correctly
        self.assertEqual(self.accounts.allowances, 1000.00) 
         
        # Checking if deductions are set correctly
        self.assertEqual(self.accounts.deductions, 500.00) 
         
