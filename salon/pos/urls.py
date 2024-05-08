from django.urls import path
from pos.views import *

urlpatterns = [ 
       path('add_to_cart/<int:p_id>',add_to_cart,name='add_to_cart'),
       path('buynow/<int:p_id>',buy_now,name='buynow'),
       path('cart',cart,name='cart'),
               
]
