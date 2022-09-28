from email import message
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User

# Create your views here.

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid  User Detail ")
            return redirect('/account/login')
    return render(request,"login.html")

def register(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User name already taken !!")
                return redirect('/account/register')
            
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password1,
                    first_name = first_name,
                    last_name = last_name,
                )
                user.save()
                auth.login(request,user)
                print("user created")
                return redirect('/')
        else:
            messages.info(request,"Password Not Matching !")
            return redirect('/account/register')             
    return render(request,"register.html")

