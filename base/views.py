from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

from django.contrib.auth import logout

from django.contrib import messages

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False) #get 6 items that are not sold to display on front page
    categories = Category.objects.all()
    return render(request,'base/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'base/contact.html')

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("You successfully created a new account!"))
            return redirect('/login/')
        else:
            messages.success(request, ("Error creating account! Please ensure your email ends in @ad.unsw.edu.au and that your passwords match"))
    else:
        form = SignupForm()
        
    
    form = SignupForm()
    
    return render(request, 'base/signup.html', {
        'form':form
    })

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('base:index')
