from django.contrib import admin
from pos.models import order,orderitem
# Register your models here.

@admin.register(order) #decorator
class orderAdmin(admin.ModelAdmin):
    list_display=['user','created_at','total_amount']
    
@admin.register(orderitem)
class orderitemAdmin(admin.ModelAdmin):
    list_display=['order','productorder','quantity'] 
