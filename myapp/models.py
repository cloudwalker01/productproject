from django.db import models
from django import forms

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    description=models.CharField(widget=forms.CheckboxInput)

    def __str__(self):
        return self.title