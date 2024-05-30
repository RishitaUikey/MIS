from django.urls import path
from pos import views

urlpatterns = [ 
       path('add_to_cart/<int:p_id>',views.add_to_cart,name='add_to_cart'),
       path('buynow/<int:p_id>',views.buynow,name='buynow'),
       path('cart',views.cart,name='cart'),
               
]
