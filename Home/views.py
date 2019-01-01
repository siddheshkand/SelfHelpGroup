from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, 'Home/login.html', {'error': 'Invalid credentials'})
    elif request.method == "GET":
        user = request.user
        if user.is_anonymous:
            return render(request, 'Home/login.html')
        else:
            return HttpResponseRedirect('/dashboard/')

    return render(request, 'Home/login.html')


def register(request):
    return render(request,'Home/register.html')


def show_dashboard(request):
    class_active = "dashboard"
    user = request.user
    # If user exists in session (i.e. logged in)
    if not user.is_anonymous:
        return render(request, 'base_dashboard.html')
    else:
        return redirect('/login/')
