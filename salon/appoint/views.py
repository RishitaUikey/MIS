from django.shortcuts import render,redirect
from services.models import service
from django.contrib.auth.models import User
from services.models import apoint,add_appoint

from django.contrib.auth.decorators import login_required
# Create your views here.

def apoint(request,p_id):
    service = service.objects.get(pk=p_id)
    add_appoint, created = Order.objects.get_or_create(user = request.user, total_amount = 0)
    orderproduct, created = 