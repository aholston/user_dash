from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.

def index(request):
    return render(request, 'userapp/index.html')

def signin(request):
    return render(request, 'userapp/signin.html')

def register(request):
    return render(request, 'userapp/register.html')

def reginfo(request):
    errors = User.objects.validate(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register')
    else:
        pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        if len(User.objects.all()) < 1 and len(Admin.objects.all()) < 1:
            newUser = Admin.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwHash)
            return redirect('/')
        else:
            newUser = Admin.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwHash)
            return redirect('/')
