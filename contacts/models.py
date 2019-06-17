from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
