from django.db import models
from django.contrib.auth import get_user_model
USER_MODEL = get_user_model()

# Create your models here.
class Facture(models.Model):
    user_id = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    total = models.FloatField(null=False, blank=False)