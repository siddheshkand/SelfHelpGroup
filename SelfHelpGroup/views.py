from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def dashboard(request):
    return render(request, 'base_dashboard.html')
