from django.shortcuts import render, redirect, get_object_or_404
from product.models import product
from django.contrib.auth.models import User
from pos.models import orderitem, order
from django.db.models import Sum,DecimalField,ExpressionWrapper,F
from django.contrib.auth.decorators import login_required

def add_to_cart(request,p_id):
    pro=product.objects.get(pk=p_id)
    u_order, created=order.objects.get_or_create(user=request.user, defaults={'total_amount':0})
    u_order_item, created=orderitem.objects.get_or_create(order=u_order,productorder=pro,defaults={'quantity': 1})

    if not created:
      u_order_item.quantity +=1
      u_order_item.save()

    u_order.total_amount +=float(pro.price) 
    u_order.save()

    return redirect('product')

# buy now
def buynow(request, p_id):
    pro = product.objects.get(pk=p_id)
    u_order = order.objects.create(user=request.user, total_amount=pro.price)
    orderitem.objects.create(order=u_order, productorder=pro, quantity =1)
    return redirect('cart')

@login_required   
def cart(request):
    u_order = order.objects.filter(user=request.user).last()
    if u_order:
        orderitems = u_order.orderitem_set.all()
        for item in orderitems:
            item.total_price = item.quantity * int(item.productorder.price)
        totalprice = u_order.total_amount
    else:
        orderitems = []
        totalprice = 0
    return render(request, 'pos/cart.html', {'order': orderitems, 'price': totalprice})

# @login_required
# def add_to_cart(request, p_id):
#     pro = product.objects.get(pk=p_id)
#     u_order = order.objects.filter(user=request.user).last()

#     if u_order:
#         order_item, created = orderitem.objects.get_or_create(order=u_order, productorder=pro, defaults={'quantity': 1})
#         if not created:
#             order_item.quantity += 1
#             order_item.save()
#     else:
#         u_order = order.objects.create(user=request.user, total_amount=0)
#         orderitem.objects.create(order=u_order, productorder=pro, quantity=1)

    # total_expression = ExpressionWrapper(F('quantity') * F('productorder__price'), output_field=DecimalField())
    # u_order.total_amount = u_order.orderitem_set.aggregate(total=Sum(total_expression))['total'] or 0
    # u_order.save()

    # return redirect('product')
# def add_to_cart(request, p_id):
#     pro = product.objects.get(pk=p_id)
#     u_order, created = order.objects.get_or_create(user=request.user, defaults={"total_amount": 0})
#     u_orderitem, created = orderitem.objects.get_or_create(order=u_order, productorder=pro, defaults={"quantity": 1})
    
#     if not created:
#         u_orderitem.quantity += 1
#         u_orderitem.save()
        
#     u_order.total_amount += float(pro.price)
#     u_order.save()
    
#     return redirect('cart') 
# # buy now
# def buynow(request, p_id):
#     pro = product.objects.get(pk=p_id)
#     u_order = order.objects.create(user=request.user, total_amount=pro.price)
#     orderitem.objects.create(order=u_order, productorder=pro, quantity =1)
#     return redirect('product')
# def cart(request):
#     u_order = order.objects.filter(user=request.user).last()
#     if u_order:
#         orderitems = u_order.orderitem_set.all()
#         totalprice = u_order.total_amount
#     else:
#         orderitems = []
#         totalprice = 0
#     for item in orderitems:
#         item.productorder.totalprice = item.quantity * int(item.productorder.price)
#     return render(request, 'pos/cart.html', {'order': orderitems, 'price': totalprice}) 
# def cart(request):
#     u_order = order.objects.filter(user=request.user).last()
    
#     if u_order:
#         orderitem= u_order.orderitem_set.all()
#         totalprice = u_order.total_amount
#     else:
#         orderitem = []
#         totalprice = 0
        
#     return render(request, 'pos/cart.html',{'order':orderitem, 'price': totalprice})

