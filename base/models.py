from turtle import title
from django.db import models

# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=255)
    body=models.CharField(max_length=255)