from django.contrib import admin
from django.urls import path
from car import views

urlpatterns = [
    path("home/",views.index, name= "index" ),
]