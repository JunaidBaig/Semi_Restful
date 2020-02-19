from django.db import models
from datetime import datetime

# Create your models here.

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

