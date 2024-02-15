'''
access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3OTgxOTk1LCJpYXQiOjE3MDc5ODE2MTgsImp0aSI6IjJjZWJhOGQzZDQ1YTQwMzhhNTA3MmJhMDFjNzJkZTYzIiwidXNlcl9pZCI6MX0.RYDM7TvdX-6wVA22sZhQ5Uw4313Ovz2TKgMpydqMOT0"

FOR Access User Use This Token

FOR Exammple 
Get Employe Details
http GET http://127.0.0.1:8000/api/employees/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3OTgxOTk1LCJpYXQiOjE3MDc5ODE2MTgsImp0aSI6IjJjZWJhOGQzZDQ1YTQwMzhhNTA3MmJhMDFjNzJkZTYzIiwidXNlcl9pZCI6MX0.RYDM7TvdX-6wVA22sZhQ5Uw4313Ovz2TKgMpydqMOT0'

For Get Token 
http POST http://127.0.0.1:8000/api/gettoken/ username='umar' password='11'

FOR Post DETAILS

Post Employee Details 
http POST http://127.0.0.1:8000/api/employees/ "Authorization: Bearer your_access_token" employee_id='your_employee_id' department='your_department' user='your_user_id'

FOR Testing Model Complete Details Below 
# 1. Import necessary modules
# 2. Import TestCase from Django's test module for testing
# 3. Import User model from django.contrib.auth.models for creating test users
# 4. Import models to be tested from the current directory
# 5. Import datetime and date modules for creating test data

# 6. Define a test case class inheriting from Django's TestCase
# 7. Override the setUp method to set up test data before each test method

# 8. Create a test user with username 'testuser' and password 'password123'
# 9. Create a test employee instance with user, employee_id, and department attributes
# 10. Create a test attendance record with the employee, check-in time, and date attributes
# 11. Create a test accounts record with the employee, month, year, basic_salary, allowances, and deductions attributes

# 12. Define a test method for checking employee creation
# 13. Assert if the employee_id attribute is set correctly
# 14. Assert if the department attribute is set correctly

# 15. Define a test method for checking attendance creation
# 16. Assert if the employee is linked correctly
# 17. Assert if the check-in time is not None
# 18. Assert if the date is set correctly

# 19. Define a test method for checking accounts creation
# 20. Assert if the employee is linked correctly
# 21. Assert if the month attribute is set correctly
# 22. Assert if the year attribute is set correctly
# 23. Assert if the basic_salary attribute is set correctly
# 24. Assert if the allowances attribute is set correctly
# 25. Assert if the deductions attribute is set correctly










'''