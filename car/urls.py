from django.contrib import admin
from django.urls import path
from car import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'car'
urlpatterns = [
    path("home/",views.index, name= "index" ),
    path("detail/<int:car_id>/",views.detail,name="detail"),
    path("about/",views.about, name= "about" ),
    path("add_car/",views.Add_car, name= "Add_car" ),
    path("contact/",views.contact, name= "contact" ),
    path("searchbar/",views.search_views,name="searchbar"),
    path("update/<int:id>/",views.update_views,name="update_views"),
    path("update_image/<int:id>/",views.update_image,name="update_image"),
    path("delete/<int:id>/",views.delete_views,name="delete_views"),
]

urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
