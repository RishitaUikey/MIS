from django.shortcuts import render,redirect
from services.models import service
from django.contrib.auth.models import User
from services.models import addproduct,add_appoint

from django.contrib.auth.decorators import login_required
# Create your views here.

# add_to_cart
def apoint(request,p_id):
    ser = service.objects.get(pk=p_id)
    add_appoint, created = add_appoint.objects.get_or_create(User = request.user, total_amount = 0)
    addproduct, created = addproduct.objects.get_or_create(add_appoint=add_appoint,add_se)