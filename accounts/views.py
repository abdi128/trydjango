from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')

        # Attempt to retrieve the user by email or username
        user = None
        try:
            user = User.objects.get(email=identifier)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=identifier)
            except User.DoesNotExist:
                user = None

        # Authenticate the user
        if user is not None:
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                return render(request, 'home.html', {})
            else:
                messages.error(request, "Invalid username/email or password!")
                return redirect('login')
        else:
            messages.error(request, "Invalid username/email or password!")
            return redirect('login')

    return render(request, 'accounts/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Logged Out Successfully!!!")
    return redirect('home')

def register_user(request):
    return render(request, 'accounts/login.html',{})