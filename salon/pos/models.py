from django.db import models
from django.contrib.auth.models import User
from product.models import product

# Create your views here.
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_order = models.ManyToManyField(product, through='orderitem')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    
    # def __str__(self) :
    #     return self.product_order.name
       
class orderitem(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    productorder = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    
