from django.contrib import admin
from django.urls import path
from car import views

urlpatterns = [
    path("home/",views.index, name= "index" ),
    path("about/",views.about, name= "about" ),
    path("add-car/",views.Add_car, name= "Add-car" ),
    path("contact/",views.contact, name= "contact" ),
]