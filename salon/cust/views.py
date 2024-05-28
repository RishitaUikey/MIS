from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from cust.forms import SignUpFrom
from django.contrib.auth.decorators import login_required
# Create your views here.

# landing page for customer 
def home(request):
    return render(request, 'customer/home.html')

# about page
def about(request):
    return render(request, 'customer/about.html')

# contact page
def contact(request):
    return render(request, 'customer/contact.html')

# product page 
# def product(request):
#     return render(request, 'customer/product.html')

# service page 
# def service(request):
#     return render(request, 'customer/services.html')

# login page 
def login_user(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('Login Successful !!!'))
            return redirect('cust_home')
        else:
            messages.success(request,('Login UN-Successful !!!'))
            return redirect('login')
    else:
        return render(request, 'customer/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,(" You have successfully loged out"))
    return render(request, 'customer/login.html')

# register page 
def register_user(request):
    form=SignUpFrom()
    if request.method == 'POST':
        form= SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('Registration Successful, and Logined in..'))
            return redirect('cust_home')
        else:
            messages.success(request,('Registration Un-Successful, try again..'))
            return redirect('register')
    return render(request, 'customer/register.html',{'form': form})

# Customer Profile page
@login_required
def userprofile(request):
    return render(request, 'customer/userprofile.html')

#custform
@login_required
def custprofile(request):
    if request.method == 'POST':
        form = customername(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custprofile')
    else:
        form = customername()
    return render(request, 'customer/custform.html',{'form':form})