from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth.hashers import make_password
from django.conf import settings


class hellow(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=15)
    fir = models.CharField(max_length=100)
    punishment = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class officer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class fir(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    crime_details = models.CharField(max_length=100)
    officer_name = models.CharField(max_length=100)


# class RegisterPage(models.Model):
# 	email = models.EmailField(max_length=100, unique= True)
# 	username = models.CharField(max_length=100)
# 	is_active = models.BooleanField(default = True)
# 	is_staff = models.BooleanField(default = False)
