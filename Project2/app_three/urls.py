"""Project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from . import views

app_name = 'app_three'

urlpatterns = [
    path('', views.index, name ='index'),
    path('other/', views.other_page, name='other'),
    re_path(r'^relative/$', views.relative, name='relative'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login_page'),
]
