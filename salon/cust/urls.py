from django.conf import settings
from django.urls import path
from cust.views import *


urlpatterns = [
    path('',home, name='cust_home'), # url for customer home / landing page
    path('about',about, name='cust_about'), # url for about
    path('contact',contact, name='cust_contact'), # url for contact
    # path('service',service, name='cust_service'), # url for service
    # path('product',product, name='cust_product'), # url for product
    path('login/',login_user, name='login'), # url for login
    path('logout/',logout_user, name='logout'),
    path('register/',register_user, name='register'), # url for register
    path('custprofile/',custprofile,name='custprofile'),
    # path('custform/',custform, name='custform'),
]
