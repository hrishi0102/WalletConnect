from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        if user.password == password:
            messages.success(request, "You have been logged in!")
            request.session['loggedin'] = True
            return redirect('/loggedin')
        return render(request, "login.html")
    return render(request, "login.html")

def register(request):
    flag = 0
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
    
        if cpassword != password:
            flag = 1
            msg = {"flag": flag}
            return render(request, "register.html", msg)
        else:
            flag = 2
            newuser = User(email=email, password=password)
            newuser.save()
        
        messages.success(request, "Your account has been created.")
        return render(request, "login.html")
        
        
    return render(request, "register.html")

def loggedin(request):
    if request.session.get('loggedin'):
        return render(request, "walletlogin.html")
    return render(request, "index.html")

def logout(request):
    if request.session.get('loggedin'):
        request.session['loggedin'] = False
    return render(request, "index.html")