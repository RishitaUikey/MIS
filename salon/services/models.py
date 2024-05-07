from django.db import models

# Create your models here.
class service(models.Model):
    name= models.CharField( max_length=50)
    detail= models.CharField( max_length=50)
    price=models.IntegerField()
    picture= models.FileField(upload_to='services/',null=True ,blank=True)
    