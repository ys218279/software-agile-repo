from django.contrib import admin
from . models import EmployeeDetails, Tickets

# Register your models here.

admin.site.register(EmployeeDetails)
admin.site.register(Tickets)