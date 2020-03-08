
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('colegio.urls')), 
]