# Employee Management System

A Django REST Framework-based Employee Management System with API support and Swagger docs.

## Features

- Employee, Attendance, Department, and Performance tracking
- API endpoints with CRUD operations
- JWT Authentication
- Swagger API Docs
- Seed fake data using Faker

## Setup Instructions

1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies:
pip install -r requirements.txt
4. Create a `.env` file using `.env.example`
5. Run migrations:
python manage.py migrate
6. Seed data:
python manage.py seed_data
7. Start the server:
python manage.py runserver

## API Docs

Visit: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
