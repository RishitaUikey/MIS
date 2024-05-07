from django.shortcuts import render
from product.models import product
# Create your views here.

def prod(request):
    prod = product.objects.all()
    return render(request, 'customer/product.html',{'pro':prod })

