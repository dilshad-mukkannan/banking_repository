from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from multiselectfield import MultiSelectField

# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    wikipedia_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = ChainedForeignKey(
        Branch,
        chained_field="district",
        chained_model_field="district",
        show_all=False,
        auto_choose=True,
        sort=True

    )

    ACCOUNT_TYPE_CHOICES = [
        ('Savings', 'Savings Account'),
        ('Current', 'Current Account'),
        # Add more account types as needed
    ]
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)

    MATERIALS_PROVIDED_CHOICES = [
        ('Debit Card', 'Debit Card'),
        ('Credit Card', 'Credit Card'),
        ('Cheque Book', 'Cheque Book'),
        # Add more material options as needed
    ]
    materials_provided = MultiSelectField(choices=MATERIALS_PROVIDED_CHOICES,default='your card')

    def __str__(self):
        return self.name
