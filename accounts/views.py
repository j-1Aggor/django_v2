from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User


def register(request):
    # check if post
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            # check if username and email are taken
            if User.objects.filter(username = username):
                messages.error(request,'Username has already been taken')
                return redirect('register')
            elif User.objects.filter(email = email):
                messages.error(request, 'email has already been taken')
                return redirect('register')
            else:
                user = User.objects.create(is_staff=False,username=username,email=email,password=password,first_name=first_name,last_name=last_name)

                user.save()
                messages.success(request,'Registered an account. Can login now')
                return redirect('login')

        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'User not found')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You have successfully logged out')
        return redirect('index')
