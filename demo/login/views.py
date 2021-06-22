from django.shortcuts import render, redirect, reverse
from login import models
from login.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from login.models import User
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect("/search_school/")
    else:
        return redirect("/login/")

def log_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect("/search_school")
        else:
            user_login_form = LoginForm()
            return render(request, 'login.html', {"login_form": user_login_form})
    elif request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/search_school/")
        else:
            return render(request, 'login.html', {"login_form": login_form})

def register(request):
    if request.method == 'GET':
        user_register_form = RegisterForm()
        return render(request, 'register.html', {"register_form": user_register_form})
    elif request.method == 'POST':
        user_register_form = RegisterForm(request.POST)
        if user_register_form.is_valid():
            username = user_register_form.cleaned_data.get("username")
            password = user_register_form.cleaned_data.get("password")
            telephone = user_register_form.cleaned_data.get("telephone")
            email = user_register_form.cleaned_data.get("email")
            User.objects.create_user(username=username, password=password, email=email, telephone=telephone)
            return redirect("/login/")
        else:
            # import pdb
            # pdb.set_trace()
            print(user_register_form.errors)
            return render(request, "register.html", {"register_form": user_register_form})

def log_out(request):
    logout(request)
    response = redirect(reverse("login"))
    response.delete_cookie('username')
    return response