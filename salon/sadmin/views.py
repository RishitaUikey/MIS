from product.models import product
from services.models import service
from staff.models import Staff
from cust.models import customer
from django.shortcuts import render,redirect
# Create your views here.

# for report
def dash(request):
    pass
# for staff
def astaff(request):
    # staff details and adding new staff
    # s= Staff.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        experience=request.POST.get('experience')
        skills=request.POST.get('skills')
        if name:
            staff=Staff.objects.create(name=name, mobile=mobile, email=email, address=address, gender=gender, experience=experience, skills=skills)
        else :
            s= Staff.objects.all() # sequential data-type
            return render(request, 'sadmin/astaff.html',{'staff' : s})

    s= Staff.objects.all() # sequential data-type
    return render(request, 'sadmin/astaff.html',{'staff' : s})

# for customer
def acust(request):

    c= customer.objects.all() # sequential data-type  
    return render(request, 'sadmin/acust.html',{'abc' : c})

# for product
def apro(request):
    if request.method=='POST':
        name=request.POST.get('name')
        detail=request.POST.get('detail')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        image= request.FILES['picture']
        if name and detail and quantity and price and image:
            store=product.objects.create(name=name, detail=detail, price=price, quantity=quantity, picture=image)
        else :
            p= product.objects.all() # sequential data-type
            return render(request, 'sadmin/apro.html',{'product' : p})
    
    p= product.objects.all() # sequential data-type
    return render(request, 'sadmin/apro.html',{'product' : p})

def delpro(request,id):
    a = product.objects.filter(id = id)
    a.delete()
    
    return redirect('/sadmin/apro')

def uppro(request,id):
    if request.method=='POST':
        name=request.POST.get('name')
        detail=request.POST.get('detail')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        image= request.FILES.get('picture')
        id=request.POST.get('id')
        if id and name and detail and price and quantity and image:
            store=product.objects.get(id=id)
            store.name=name
            store.detail=detail
            store.price=price
            store.quantity=quantity
            if image:
                store.picture=image
            store.save()
            
            
            return redirect('/sadmin/apro')
        else :
            pass
    
    s= product.objects.get(pk=id)
    return render(request,'sadmin/edit_product.html',{'pro':s})

# for service
def aserv(request):
    if request.method=='POST':
        name=request.POST.get('name')
        detail=request.POST.get('detail')
        price=request.POST.get('price')
        image= request.FILES['picture']
        if name and detail and price and image:
            aserv=service.objects.create(name=name, detail=detail, price=price, picture=image)
        else :
            r = service.objects.all() # sequential data-type
            return render(request, 'sadmin/aserv.html',{'service' : r})
    
    r= service.objects.all() # sequential data-type
    return render(request, 'sadmin/aserv.html',{'service' : r})

def delserv(request,id):
    d = service.objects.filter(id = id)
    d.delete()
    
    return redirect('/sadmin/aserv')

def upserv(request,id):
    if request.method=='POST':
        name=request.POST.get('name')
        detail=request.POST.get('detail')
        price=request.POST.get('price')
        image= request.FILES.get('picture')
        id=request.POST.get('id')
        if id and name and detail and price and image:
            store=service.objects.get(id=id)
            store.name=name
            store.detail=detail
            store.price=price
            if image:
                store.picture=image
            store.save()
            
            return redirect('/sadmin/aserv')
        else :
            pass
    
    s= service.objects.get(pk=id)
    return render(request,'sadmin/edit_service.html',{'ser':s})