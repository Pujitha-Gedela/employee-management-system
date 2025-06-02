from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee, Performance
from attendance.models import Attendance
import random
from datetime import timedelta, date

class Command(BaseCommand):
    help = 'Seed the database with dummy employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        self.stdout.write(self.style.NOTICE('Seeding data...'))

        # Clear old data
        Attendance.objects.all().delete()
        Performance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

        # Create 5 departments
        departments = []
        for _ in range(5):
            dept = Department.objects.create(name=fake.job())
            departments.append(dept)

        # Create 50 employees
        for _ in range(50):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(departments)
            )

            # Create 10 attendance records for each employee
            for _ in range(10):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_between(start_date='-90d', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )

            # Add 1 performance review per employee
            Performance.objects.create(
                employee=emp,
                rating=random.randint(1, 5),
                review_date=date.today() - timedelta(days=random.randint(0, 365))
            )

        self.stdout.write(self.style.SUCCESS('Seeding complete!'))
