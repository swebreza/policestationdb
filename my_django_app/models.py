from django.db import models


class hellow(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=15)
    fir = models.CharField(max_length=100)
    punishment = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
