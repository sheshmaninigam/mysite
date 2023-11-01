"""
URL configuration for mysite project.

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
from django.urls import path,include
from users import views
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = "EMON Admin"
admin.site.site_title = "EMON Admin Portal"
admin.site.index_title = "Welcome to Emon Admin Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("car/",include("car.urls")),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("profile/",views.profile_views,name="profile"),
    path("profile_edit/<int:id>/",views.profile_edit,name="profile_edit"),
#     path('<int:pk>/',views.ProfileUpdateView.as_view, name='update'),
]

urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













