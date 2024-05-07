from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from staff.forms import SignUpFrom
# Create your views here.
def staffhome(request):
    return render(request, 'staff/home.html')

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
            return redirect('staff/login')
    else:
        return render(request, 'staff/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,(" You have successfully loged out"))
    return render(request, 'staff/login.html')

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
            return redirect('staff/register')
    return render(request, 'staff/register.html',{'form': form})