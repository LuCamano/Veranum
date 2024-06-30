from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono', 'comuna', 'imagen']
    list_filter = ['comuna']

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['numero', 'tipo']
    list_filter = ['tipo']

@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'cantidadCamas', 'cantidadBanos', 'hotel']
    search_fields = ['nombre', 'precio']

@admin.register(ServicioAdicional)
class ServicioAdicionalAdmin(admin.ModelAdmin):
    list_display = ['nombre']