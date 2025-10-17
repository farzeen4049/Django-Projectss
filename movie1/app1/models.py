from django.db import models

# Create your models here.

class Moviedetail(models.Model):
     title=models.CharField(max_length=100)
     description=models.TextField()
     language=models.CharField(max_length=100)
     year=models.IntegerField()
     directory=models.CharField(max_length=100)
     image=models.ImageField(upload_to='images')
