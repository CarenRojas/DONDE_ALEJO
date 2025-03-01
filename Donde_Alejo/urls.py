"""
URL configuration for Donde_Alejo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from dondealejo import views




from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('email', views.email, name='email'),
    path('bienvenidos', views.bienvenidos, name='bienvenidos'),
    path('almuerzo', views.almuerzo, name='almuerzo'),
    path('cafeteria', views.cafeteria, name='cafeteria'),
    path('quienes_somos', views.quienes_somos, name='quienes_somos'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('carrito', views.carrito, name='carrito'),
    path('sesion', views.sesion, name='sesion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

