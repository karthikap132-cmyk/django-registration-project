from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
# Create your models here.
