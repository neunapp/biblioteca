"""
    biblioteca URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.autor.urls')),
    re_path('', include('applications.libro.urls')),
    re_path('', include('applications.lector.urls')),
]
