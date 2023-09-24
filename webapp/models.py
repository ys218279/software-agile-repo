from django.db import models
from django.contrib.auth.models import User


#Employee details

class EmployeeDetails(models.Model):   #rename to user details record
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=225)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=225)
    postcode = models.CharField(max_length=200)
    country = models.CharField(max_length=125)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create a seccond table 

ITEMS = (
    ('Monitor','monitor'),
    ('Laptop','laptop'),
    ('Desktop','desktop'),
    ('Keyboard','keyboard'),
    ('Mouse','mouse'),
)

LOCATION_USE = (
    ('Home','home'),
    ('Office','office'),
)

class Tickets(models.Model):
    item = models.CharField(max_length=8, choices=ITEMS)
    location_use = models.CharField(max_length=6, choices=LOCATION_USE)
    date_hired = models.DateField(max_length=8)
    date_returned = models.DateField(max_length=8)

