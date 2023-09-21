from django.db import models

class Record(models.Model):
    creation_date = models.DateField(auto_now_add=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=225)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=225)
    provinence = models.CharField(max_length=200)
    country = models.CharField(max_length=125)

    def __str__(self):
        return self.first_name + "   " + self.last_name

# Create a seccond table 