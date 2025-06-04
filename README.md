# Employee Management System

A backend application built with **Django** and **Django REST Framework** to manage employees, their attendance, departments, and performance.  
This project includes secure login using JWT tokens, interactive API documentation via Swagger UI, and a command to generate fake data for testing using Faker.

---

## Features

- Full CRUD (Create, Read, Update, Delete) APIs for:
  - Employees
  - Departments
  - Attendance
  - Performance Reviews
- JWT Authentication (secure login for API access)
- Swagger UI for testing APIs in the browser
- Seed command to auto-generate 50+ fake employees with related data

---

## Technologies Used

- Python 3.11+
- Django 5+
- Django REST Framework
- Simple JWT for authentication
- drf-yasg for Swagger UI
- Faker for generating test data

---

## Getting Started

Follow the steps below to set up and run the project on your local machine.

1. Clone the Repository
git clone https://github.com/your-username/employee-management-system.git
cd employee-management-system

2. Create and Activate a Virtual Environment
Create a virtual environment to keep project dependencies isolated.
for windows:
python -m venv env
env\Scripts\activate
3.Install Required Dependencies
Use the requirements.txt file to install all Python packages needed to run the project.

bash
pip install -r requirements.txt
4. Set Up Environment Variables
Create a file named .env in the root directory and add environment variables by copying the contents of .env.example.
5.Apply Database Migrations
Run the following command to create all necessary tables in the database:

bash
python manage.py migrate
6.Create a Superuser Account
This will allow you to access Django’s admin panel and authenticate through the API.

bash
python manage.py createsuperuser
Enter your username, email, and password when prompted.

7. Seed the Database with Fake Data
Use this command to populate the database with 50 fake employees and related records (departments, attendance, performance):

bash
python manage.py seed_data
8. Start the Development Server
Run the server to start using the project locally.

bash
python manage.py runserver
Then open your browser and go to:
Once running, open these URLs in your browser:

🔹 Swagger API Docs:
http://127.0.0.1:8000/swagger/ (only works while the server is running locally)

🔹 Django Admin Panel:
http://127.0.0.1:8000/admin/

Authentication (JWT)
Go to the /api/token/ route in Swagger.

Enter your superuser credentials to receive access and refresh tokens.

Click the Authorize button and enter:

Bearer your_access_token_here
Now you'll be able to test all protected routes.
Once the server is running, go to:
http://127.0.0.1:8000/swagger/
You can test GET, POST, PUT, and DELETE operations directly in the browser.


You’ll see a full list of API endpoints and be able to test them.

employee-management-system/
│
├── attendance/               # Attendance models, views, serializers, URLs
├── employees/                # Employees, Departments, Performance logic
│   └── management/
│       └── commands/
│           └── seed_data.py  # Fake data seeding script
├── employee_project/         # Main project settings and URLs
├── templates/ (optional)     # Chart.js or frontend templates
├── .env.example              # Sample environment variables
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

