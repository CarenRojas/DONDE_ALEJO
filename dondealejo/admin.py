from django.contrib import admin
from dondealejo.models import Producto
from django.contrib.admin.sites import AlreadyRegistered

# Aquí solo registramos una vez
class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('nombre', 'precio', 'fecha_creacion','foto')
    list_display_links = ('nombre',)

admin.site.register(Producto, ProductoAdmin)
from .models import CarritoItem

class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'usuario', 'sesion_id', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('producto__nombre', 'usuario__username')

try:
    admin.site.register(CarritoItem, CarritoItemAdmin)
except AlreadyRegistered:
    pass

from .models import Orden, OrdenItem

class OrdenItemInline(admin.TabularInline):
    model = OrdenItem
    extra = 0
    readonly_fields = ('producto', 'precio', 'cantidad')

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono', 'total', 'pagado', 'fecha_creacion')
    list_filter = ('pagado', 'fecha_creacion')
    search_fields = ('nombre', 'email')

try:
    admin.site.register(Orden, OrdenAdmin)
except AlreadyRegistered:
    pass



from django.contrib import admin
from .models import Reserva, Domicilio

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha', 'hora', 'cantidad_personas', 'creada')
    search_fields = ('nombre', 'email', 'telefono')
    list_filter = ('fecha', 'hora')
    ordering = ('-creada',)

@admin.register(Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha')
    search_fields = ('nombre', 'email', 'telefono')
    list_filter = ('fecha',)
    readonly_fields = ('fecha',)
