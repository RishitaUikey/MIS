from django.shortcuts import render, redirect, get_object_or_404
from product.models import product
from django.contrib.auth.models import User
from pos.models import orderitem, order

from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, p_id):
    pro = product.objects.get(pk=p_id)
    u_order, created = order.objects.get_or_create(user=request.user, defaults={"total_amount": 0})
    u_orderitem, created = orderitem.objects.get_or_create(order=u_order, productorder=pro, defaults={"quantity": 1})
    
    if not created:
        u_orderitem.quantity += 1
        u_orderitem.save()
        
    u_order.total_amount += float(pro.price)
    u_order.save()
    
    return redirect('product') 

@login_required
def buynow(request, p_id):
    pro = product.objects.get(pk=p_id)
    u_order, created = order.objects.get_or_create(user=request.user, defaults={"total_amount": 0})
    u_orderitem, created = orderitem.objects.get_or_create(order=u_order, productorder=pro, defaults={"quantity": 1})
    
    if not created:
        u_orderitem.quantity = 1
    u_orderitem.save()
    
    u_order.total_amount = float(pro.price)
    u_order.save()
    
    return redirect('product') 

# @login_required
# def add_to_cart(request, p_id):
#     pro = product.objects.get(pk=p_id)
#     u_order, created = order.objects.get_or_create(user = request.user, defaults={"total_amount" : 0})
#     u_orderitem, created = orderitem.objects.get_or_create(order=u_order, productorder = pro,defaults={"quantity": 1})
    
#     if not created :
#         u_orderitem.quantity +=1
#         u_orderitem.save()
        
#     u_order.total_amount += float(pro.price)
#     u_order.save()
    
#     return redirect('product') # card

# # buy now
# def buynow(request, p_id):
#     pro = product.objects.get(pk=p_id)
#     u_order = order.objects.create(user=request.user, total_amount=pro.price)
#     orderitem.objects.create(order=u_order, productorder=pro, quantity =1)
#     return redirect('product')

# @login_required    
# def cart(request):
#     order = order.objects.filter(user=request.user).last()
    
#     if order:
#         orderitem= order.orderitem_set.all()
#         totalprice = order.total_amount
#     else:
#         orderitem = []
#         totalprice = 0
        
#     return render(request, 'cart.html',{'order':orderitem, 'price': totalprice})