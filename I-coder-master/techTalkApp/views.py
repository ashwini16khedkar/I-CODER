from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import login as login_auth, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.
def homePage(request):
    return HttpResponse("Hello World")

def ContactUs(request):
    if request.method == "POST":
        data = ContactUs(name=request.POST['name'],email=request.POST['email'],message=request.POST['message'])
        data.save()
        messages.success(request,"Your query send to admin Successfully please check your email for further information")
    return render(request,'contactUs.html')

def login(request):
    if request.method == "POST":
        user = authenticate(username=str(request.POST['username']),password=request.POST['password'])
        if user is not None:
            login_auth(request,user)
            return redirect("/homepage/")
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect("/login/")
    return render(request, 'login.html')

