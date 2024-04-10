from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'home.html', context)

def signup_page(request):
    context = {}
    return render(request, 'signup.html', context)

def login_page(request):
    context = {}
    return render(request, 'login.html', context)

def reset_password(request):
    context = {}
    return render(request, 'password_reset.html', context)

def set_new_password(request):
    context = {}
    return render(request, 'set_password.html', context)

def change_password(request):
    context = {}
    return render(request, 'change_password.html', context)