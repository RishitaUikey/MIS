from django.shortcuts import render
from services.models import service
# Create your views here.

def servi(request):
    ser = service.objects.all()
    return render(request, 'customer/services.html',{'ser':ser})

def servidetail(request, id):
    ser = service.objects.get(pk = id)
    return render(request, 'servi/s_details.html',{'ser':ser})