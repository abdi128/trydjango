from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.forms import UserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

"""def login_user(request):
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
                #messages.success(request, "You have logged in successfully!")
                return redirect('home')
                #messages.error(request, "Invalid username/email or password!")
                return redirect('login')
        else:
            #messages.error(request, "Invalid username/email or password!")
            return redirect('login')

    return render(request, 'accounts/login.html', {})"""

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have logged in successfully!")
            return redirect('home')
        """else:
            messages.error(request, "Something went wrong, Try Again")
            return render(request, "accounts/login.html", context)"""
    else:
        form = AuthenticationForm(request)
    context = { "form":form }
    return render(request, "accounts/login.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Logged Out Successfully!!!")
    return redirect('home')

def register_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('login')
    return render(request, 'accounts/register.html', { "form": form })