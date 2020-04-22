from django.contrib import admin
from django.urls import path, include
from apps.api import mahasiswa

urlpatterns = [
    #mahasiswa
    path('login', mahasiswa.login, name='api-login')
]

