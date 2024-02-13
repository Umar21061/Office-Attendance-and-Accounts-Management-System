# Importing necessary modules
from django.shortcuts import render
from pymongo import MongoClient

# Defining the home view function
def home(request):
    # Connect to MongoDB
    client = MongoClient('localhost', 27017)
    # Accessing the 'office' database
    db = client['office']
    # Accessing the 'employees' collection
    employees_collection = db['employees']

    # Retrieving all employees from the collection
    employees = employees_collection.find()

    # Handling POST request
    if request.method == 'POST':
        # Retrieving the selected employee's name from the POST data
        selected_employee_name = request.POST.get('employee')
        # Finding the selected employee in the collection
        selected_employee = employees_collection.find_one({'name': selected_employee_name})
        # Rendering the 'employee_details.html' template with the selected employee's data
        return render(request, 'employee_details.html', {'employee': selected_employee})

    # Rendering the 'home.html' template with all employees' data
    return render(request, 'home.html', {'employees': employees})
