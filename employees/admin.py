from django.contrib import admin

# Register your models here.
from .models import Department, Employee, Performance

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Performance)
