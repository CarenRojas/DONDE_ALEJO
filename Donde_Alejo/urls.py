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


# from web.views import perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('bienvenidos', views.bienvenidos, name='bienvenidos'),
    path('almuerzo', views.almuerzo, name='almuerzo'),
    path('desayunos', views.desayunos, name='desayunos'),
    path("solicitar_domicilio/", views.solicitar_domicilio, name="solicitar_domicilio"),
    path("domicilios", views.solicitar_domicilio, name="domicilios"),
    path('cafeteria', views.cafeteria, name='cafeteria'),
    path('quienes_somos', views.quienes_somos, name='quienes_somos'),
    path('reservar', views.reservar, name='reservar'),
    path('manual', views.manual, name='manual'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('restablecer/', views.restablecer, name='restablecer'),
    path('cambiar_contrasena/<uidb64>/<token>/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('password_changed/', views.password_changed, name='password_changed'),
    path('sesion', views.sesion, name='sesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('pasarela/', views.pasarela, name='pasarela'),
    path('confirmacion/<int:orden_id>/', views.confirmacion, name='confirmacion'),
    path('historial/', views.historial_domicilios, name='historial_domicilios'),
    path('historial-ordenes/', views.historial_ordenes, name='historial_ordenes'),
    path('cambiar_estado/<int:orden_id>/', views.cambiar_estado_orden, name='cambiar_estado_orden'),

    
    path('perfil/', views.perfil, name='perfil'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
