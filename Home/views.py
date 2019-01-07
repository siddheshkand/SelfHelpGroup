from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . import forms


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/dashboard/')
        else:
            return render(request, 'Home/login.html', {'error': 'Invalid credentials'})
    elif request.method == "GET":
        user = request.user
        if user.is_anonymous:
            return render(request, 'Home/login.html')
        else:
            return HttpResponseRedirect('/home/dashboard/')

    return render(request, 'Home/login.html')


def register(request):
    make_class_active = "members"
    form = forms.RegistrationForm()
    return render(request, 'Home/register.html', {'form': form, 'make_class_active': make_class_active})


def show_dashboard(request):
    make_class_active = "dashboard"
    user = request.user
    # If user exists in session (i.e. logged in)
    if not user.is_anonymous:
        return render(request, 'base_dashboard.html', {'make_class_active': make_class_active})
    else:
        return redirect('/home/login/')


def member(request):
    make_class_active = "members"
    return render(request, 'Home/member.html', {'make_class_active': make_class_active})


def collection(request):
    make_class_active = "collection"
    return render(request, 'Home/collection.html', {'make_class_active': make_class_active})
