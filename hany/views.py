from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'employees/about.html')

# Contact page view


def contact(request):
    return render(request, 'employees/contact.html')

# Example: Add Employee View (for form submissions)


def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        # Example: Save to DB (only if you have a model called Employee)
        # Employee.objects.create(name=name, role=role)
        return redirect('index')  # redirect to homepage
    return render(request, 'add_employee.html')


def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = user.userprofile  # Assuming UserProfile is linked to User
        return render(request, 'dashboard.html', {'profile': profile})
    else:
        return redirect('login')  # Redirect to login if not authenticated


def edit_profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = user.userprofile  # Assuming UserProfile is linked to User

        if request.method == 'POST':
            profile.phone_number = request.POST.get('phone_number')
            profile.address = request.POST.get('address')
            profile.save()
            # Redirect to user profile after saving
            return redirect('user_profile')

        return render(request, 'edit_profile.html', {'profile': profile})
    else:
        return redirect('login')  # Redirect to login if not authenticated


def logout(request):
    if request.user.is_authenticated:
        from django.contrib.auth import logout as auth_logout
        auth_logout(request)
    return redirect('index')  # Redirect to homepage after logout


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Example: Create user (only if you have a User model)
        # from django.contrib.auth.models import User
        user = User.objects.create_user(
            username=username, password=password, email=email)
        return redirect('login')  # redirect to login after registration
    return render(request, 'register.html')
