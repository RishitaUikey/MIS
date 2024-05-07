from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField( max_length=50)
    detail = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    
    picture= models.FileField(upload_to='product/',null=True ,blank=True)
    