from django.db import models

class countrys(models.Model):
   country  = models.CharField(max_length=100)
   languages = models.CharField(max_length=100)

# Create your models here.
