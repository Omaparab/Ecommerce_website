from django.db import models
from django.core.validators import RegexValidator, EmailValidator

# Create your models here.

class signup_page(models.Model):
    Username = models.CharField(max_length=30)
    Email = models.CharField(max_length=30, unique=True) 
    Password = models.CharField(max_length=30)

class purchase(models.Model):
    Full_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254, validators=[EmailValidator()])
    City = models.CharField(max_length=100)
    Zip_code = models.CharField(max_length=10, validators=[
        RegexValidator(
            regex=r'^\d{5}(-\d{4})?$',
            message='ZIP code must be in the format: 12345 or 12345-6789.',
        )
    ])
    Phone = models.CharField(max_length=15, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message='Phone number must be in the format: +999999999 or 999999999.',
        )
    ])

class id(models.Model):
    Order_id = models.CharField(max_length=100)