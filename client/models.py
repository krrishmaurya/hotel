
from django.db import models

class Booking(models.Model):
    customer_name=models.CharField(max_length=20)
    customer_age=models.IntegerField()
    contact_no=models.CharField(max_length=12)
    email=models.EmailField()
    booking_date=models.DateField()
