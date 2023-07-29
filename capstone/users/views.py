from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    """Defines the html request that will be triggered when a user gets to the home page"""
    return render(request, 'user/home.html')

def register(request):
    """This function will check if a user has a valid account or not and will trigger an account creation form"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'user/register.html', context)

def about_us(request):
    return render(request, 'user/about_us.html')

def login(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')