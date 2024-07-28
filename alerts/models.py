
# Create your models here.
from django.db import models
from django.conf import settings

class Alert(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.CharField(max_length=10)
    target_price = models.FloatField()
    current_price = models.FloatField()
    status = models.CharField(max_length=10, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
