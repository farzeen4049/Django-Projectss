import random

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=20,null=True)
    is_verified=models.BooleanField(default=False) #to check weather user acct is verified or not
    otp=models.CharField(max_length=10,null=True)  #to store otp in backend table (CustomUser)


    def generate_otp(self):
        otp=str(random.randint(1000,9999))+str(self.id)
        self.otp=otp
        self.save()