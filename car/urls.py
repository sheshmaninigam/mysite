from django.contrib import admin
from django.urls import path
from car import views

urlpatterns = [
    path("home/",views.index, name= "index" ),
    path("about/",views.about, name= "about" ),
    path("services/",views.services, name= "services" ),
    path("contact/",views.contact, name= "contact" ),
]