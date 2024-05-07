from django.db import models

# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    
    #to check when the user or the customer added to our list
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)