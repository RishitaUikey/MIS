from django.db import models
from django.contrib.auth.models import User
from services.models import service
# Create your models here.

class apoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_service = models.ManyToManyField(service, through='add_appoint')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self) :
        return self.id
    
class add_appoint(models.Model):
    apoint = models.ForeignKey(apoint, on_delete=models.CASCADE)
    add = models.ForeignKey(service, on_delete=models.CASCADE)

    
    def __str__(self) :
        return self.apoint.id    