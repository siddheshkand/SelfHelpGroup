from django.shortcuts import render


def index(request):
    return render(request, 'new_base.html')


def dashboard(request):
    return render(request, 'new_dashboard_base.html')


def form(request):
    return render(request, 'new_form_base.html')
