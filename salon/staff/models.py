from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=50)
    mobile= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address= models.TextField()
    gender= models.CharField(max_length=50) # choice field
    experience= models.IntegerField()
    skills = models.TextField() # choice field
    
    
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,blank=True)