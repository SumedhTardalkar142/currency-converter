from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
from .currency_data import currency_of_country



def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']


        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
    
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')


    return render(request, 'login.html' , context = {'page' : 'Currency Convertor | Login'})

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username Already Taken")
            return redirect('/register')
        
        user = User.objects.create(
        username = username
        )

        user.set_password(password)

        user.save()

        messages.info(request, "Account Created Succesfully")


        return redirect("/register/")
    
    return render(request, 'register.html' , context = {'page' : 'Currency Convertor | Register'})

@login_required(login_url="/login/")
def home_page(request):
    dropdown = None
    amount = 1
    if request.method == "POST":
        dropdown = request.POST.get('base') or "EUR"
        dropdown2 = request.POST.get('target') or "INR"
        amount = request.POST.get('amount')

        print(dropdown)
        print(dropdown2)

    if dropdown != None:
        urls = f"https://v6.exchangerate-api.com/v6/4cbb60203b477ff1a6c8c04d/pair/{dropdown}/{dropdown2}/{amount}"
    else:
        urls = f"https://v6.exchangerate-api.com/v6/4cbb60203b477ff1a6c8c04d/pair/EUR/USD/1"
    
    print(urls)
    response = requests.get(urls)
    data = response.json()

    base = data['base_code']
    target = data['target_code']
    conversion_rate = data['conversion_rate']
    conversion_result = data['conversion_result']
    context = {'currency_of_country': currency_of_country, 'base' : base, 'target' : target, 
               'result1' : conversion_rate, 'result2' : conversion_result, 
               'page' : 'Currency Convertor | Home', 'amount' : amount}
    return render(request, 'home.html', context)

def supported_currencies(request):
    context = {
        'currency_to_country': currency_of_country,
        'page' : 'Currency Convertor | Supported Currencies' 
    }
    return render(request, 'supported currencies.html', context)

def about_page(request):
    return render(request, 'about.html', context={'page' : 'Currency Convertor | About' })