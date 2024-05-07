from django.contrib import admin
from product.models import product
# Register your models here.

@admin.register(product) # decorator
class productAdmin(admin.ModelAdmin):
    list_display=['name', 'detail','price', 'quantity']