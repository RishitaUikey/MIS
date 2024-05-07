from django.urls import path
from product.views import prod

urlpatterns = [
    path('', prod,name='product'),
]