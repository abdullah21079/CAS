"""
URL configuration for Canteen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
import demo.views
import django.contrib.auth.views as auth_view


urlpatterns = {
    path('admin/', admin.site.urls),
    path('index/', demo.views.index, name='index'),
    path('landing/', demo.views.landing, name='landnig'),

    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', demo.views.register, name='register'),

    path('aboutus/', demo.views.aboutus, name='aboutus'),
    path('logout/', demo.views.logout, name='logout'),
    path('firRegistration/', demo.views.firRegistration, name='firRegistration'),
    path('showupdate/', demo.views.showupdate, name='showupdate'),
    path('addinfo/', demo.views.addinfo, name='addinfo'),
    path('emergencyContact/', demo.views.emergencyContact, name='emergencyContact'),
    path('crimeRecord/', demo.views.crimeRecord, name='crimerecord'),

}
