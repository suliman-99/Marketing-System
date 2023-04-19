from django.db import models
from django.contrib.auth.models import User


class Marketer(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    withdrawal_threshold = models.PositiveIntegerField()
    commission = models.DecimalField(max_digits=2, decimal_places=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    reference_link = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.id} - {self.user.username} ({self.user.first_name} {self.user.last_name})'
    
class Product(models.Model):
    price = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()
    marketers = models.ManyToManyField(Marketer, related_name='products')

    def __str__(self):
        return f'{self.id} - {self.title} ({self.type})'

Product.marketers.through._meta.verbose_name = 'Sell'
Product.marketers.through._meta.verbose_name_plural  = 'Sales'

