from django.shortcuts import render, redirect, get_object_or_404
from product.models import product
from django.contrib.auth.models import User
from pos.models import OrderItem, Order

from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, p_id):
    pro = get_object_or_404(product, pk=p_id)
    order, created = Order.objects.get_or_create(user = request.user, total_amount = 0)
    orderitem, created = OrderItem.objects.get_or_create(order=order, productorder = pro)
    
    if not created :
        orderitem.quantity +=1
        orderitem.save()
        
    order.total_amount += pro.price
    order.save()
    
    return redirect('cart')

# buy now
def buy_now(request, p_id):
    pro = get_object_or_404(product,pk=p_id)
    order = Order.objects.create(user=request.user, total_amount=pro.price)
    OrderItem.objects.create(order=order, productorder=pro, quantity =1)
    return redirect('details')

@login_required    
def cart(request):
    order = Order.objects.filter(user=request.user).last()
    
    if order:
        orderitem= order.OrderItem_set.all()
        totalprice = order.total_amount
    else:
        orderitem = []
        totalprice = 0
        
    return render(request, 'cart.html',{'order':orderitem, 'price': totalprice})
