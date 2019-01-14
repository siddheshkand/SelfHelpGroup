"""SelfHelpGroup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Collection
    2. Add a URL to urlpatterns:  path('', Collection.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

app_name = 'Home'
urlpatterns = [
    path('dashboard/', views.show_dashboard, name='show_dashboard'),
    path('member/', views.member, name='member'),
    path('member/register', views.register, name='register'),
    path('collection/', views.collection, name='collection'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
