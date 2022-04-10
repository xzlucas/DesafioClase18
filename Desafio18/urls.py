from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from Desafio18.views import familiaresForm

urlpatterns = [
        path('agregar-familiar/', familiaresForm, name="agrega"),

]