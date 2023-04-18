from django.db import models

class Product(models.Model):
    price = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()


class Marketer(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]

    balance = models.PositiveIntegerField()
    withdrawal_threshold = models.PositiveIntegerField()
    commission = models.DecimalField(max_digits=3, decimal_places=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    reference_link = models.CharField(max_length=255)



