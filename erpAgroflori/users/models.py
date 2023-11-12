from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

# Create your models here.
class User (AbstractUser):
    pass

class Person (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=5, blank= True, null=True)
    birth_date = models.DateField(auto_now=False, blank= True, null=True)
    date_joined_agr = models.DateField(db_comment="Date of entrance to Agroflori.", blank= True, null=True)
    phone = PhoneNumberField(region='BO', blank= False, null=False)
    emergency_phone = PhoneNumberField(blank=False, region='BO', null=False)
    emergency_name = models.CharField(max_length=100, blank= False, null=False)
    has_paid = models.BooleanField(blank=True, null=True, db_comment="The volunteer has paid the entrance fee.")
    profile_pic = models.ImageField(upload_to='media/profile_pics', blank=True, null=True)
    
class WorkRecord(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="worker")
    date = models.DateField(auto_now_add=False, default= date.today, null=False, blank=False)
    description = models.CharField(max_length=300, blank=False, null=False)



