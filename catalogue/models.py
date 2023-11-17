from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    img = models.CharField(max_length=300, blank=False, null=False)
    price = models.FloatField()