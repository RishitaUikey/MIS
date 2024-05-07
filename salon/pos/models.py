from django.db import models
from django.contrib.auth.models import User
from product.models import product

# Create your views here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_order = models.ManyToManyField(product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self) :
        return self.id
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    productorder = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self) :
        return self.order.id
