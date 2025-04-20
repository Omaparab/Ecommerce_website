from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages  
from .models import signup_page, purchase, id
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
import random


def home(request):
    
    login_visited = request.session.get('login_visited', False)

    if login_visited == False:
        messages.info(request, 'Login')
    else:
        messages.info(request, 'Logout')

    return render(request, 'main/home.html', {'login_visited': login_visited})


def login(request):
    messages.info(request, '')
    request.session['login_visited'] = False
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        try:
            user = signup_page.objects.get(Email=email)
        except signup_page.DoesNotExist:
            messages.info(request, 'No account found with this email.')
            return redirect('login')

        if user.Password != password:
            messages.info(request,'Incorrect password. Please try again.')
            return redirect('login') 
        else:
            request.session['login_visited'] = True
            return redirect('home')  

    return render(request, 'main/login.html')


def signup(request):

    if request.method == 'POST':
        Username = request.POST.get("Username")
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")
        Cpassword = request.POST.get("Cpassword")
        
        if Email.endswith('@gmail.com'):

            if len(Username)<4:
                messages.info(request,'Username should have atleast 4 characters')
                return redirect('signup')
            elif len(Password)<6:
                messages.info(request, 'Password should have atleast 6 characters')
                return redirect('signup')
            else:
                if Password == Cpassword:
                    if signup_page.objects.filter(Email=Email).exists():
                        messages.info(request,'Account with this email already exists...')
                        return redirect('signup')
                    
                    person = signup_page(Username=Username, Email=Email, Password=Password)
                    person.save()
                    return redirect('login')
                        
                else:
                    messages.info(request,'Passwords do not match...')
                    return redirect('signup')
        else:
            messages.info(request,'Enter the email with correct domain: xyz@gmail.com')
            return redirect('signup')
        
    return render(request,'main/signup.html')

def logout_confirmation(request):
    request.session['login_visited'] = False
    return render(request, 'main/logout_confirmation.html')

def cart(request):
    return render(request, 'main/cart.html')

def checkout(request):
    return render(request, 'main/checkout.html')

def confirmation(request):
    return render(request, 'main/confirmation.html')

def proceed(request):
    ID = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    Order = id(Order_id=ID)
    Order.save()

    return render(request, 'main/proceed.html',{'ID': ID})

def buy(request):
    if request.method == 'POST':
        Full_name = request.POST.get("full-name")
        Email = request.POST.get("email")
        City = request.POST.get("city")
        Zip_code = request.POST.get("zip-code")
        Phone = request.POST.get("phone")

        if Email.endswith('@gmail.com'):
            if len(Phone) == 10 and Phone.isdigit():
                buy = purchase(Full_name=Full_name, Email=Email, City=City, Zip_code=Zip_code, Phone=Phone)
                buy.save()
                return redirect('proceed')
            else:
                messages.info(request,"Enter an appropriate Phone number")
        else:
            messages.info(request,"Enter the email with correct domain: xyz@gmail.com")
    
    return render(request, 'main/buy.html')


def drafter(request):

    login_visited = request.session.get('login_visited', False)
    return render(request, 'products/drafter.html', {'login_visited': login_visited})


def calci(request):
    login_visited = request.session.get('login_visited', False)
    return render(request, 'products/calci.html', {'login_visited': login_visited})


def folder(request):
    login_visited = request.session.get('login_visited', False)
    return render(request, 'products/folder.html', {'login_visited': login_visited})


def geometry(request):
    login_visited = request.session.get('login_visited', False)
    return render(request, 'products/geometry.html', {'login_visited': login_visited})


def punch(request):
    login_visited = request.session.get('login_visited', False)
    return render(request, 'products/punch.html', {'login_visited': login_visited})


def raspberry(request):
    login_visited = request.session.get('login_visited', False)
    return render(request, 'products/raspberry.html', {'login_visited': login_visited})


def sheetholder(request):
    login_visited = request.session.get('login_visited', False)
    return render(request, 'products/sheetholder.html', {'login_visited': login_visited})


def stapler(request):
    login_visited = request.session.get('login_visited', False)
    return render(request, 'products/stapler.html', {'login_visited': login_visited})


