"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from todoapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/',register_view,name='users-register'),
    path('login/',auth_views.LoginView.as_view(template_name='todoapp/login.html'),name='users-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='todoapp/logout.html'),name='users-logout'),
    
    
    path('', homeview,name= 'home'),
    path('remove/<int:item_id>',removeview),
    path('complete/<int:item_id>',completeview),
    path('about/', aboutview),
    path('htmldemo/',htmldemoview),
    
    
    path("__reload__/", include("django_browser_reload.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
