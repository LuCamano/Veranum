from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_hoteles, name='listado_hoteles'),
    path('agregar-hotel/', views.agregar_hotel, name='agregar-hotel'),
    path('eliminar-hotel/<id>/', views.eliminar_hotel, name='eliminar-hotel'),
    path('modificar-hotel/<id>/', views.modificar_hotel, name='modificar-hotel'),
    path('hotel/<id>/', views.vista_hotel, name='hotel'),
    path('hotel/<id>/habitaciones/', views.listado_habitaciones, name='habitaciones'),
    path('hotel/<id>/habitaciones/agregar/', views.agregar_habitacion, name='agregar-habitacion'),
    path('hotel/<id>/habitaciones/modificar/<hid>/', views.modificar_habitacion, name='modificar-habitacion'),
    path('hotel/<id>/habitaciones/eliminar/<hid>/', views.eliminar_habitacion, name='eliminar-habitacion'),
    path('hotel/<id>/tipos-habitaciones/', views.tipo_habitaciones, name='tipo-habitaciones'),
    path('hotel/<hid>/tipos-habitaciones/agregar/', views.agregar_tipo, name='agregar-tipo'),
    path('hotel/<hid>/tipos-habitaciones/modificar/<tid>/', views.modificar_tipo, name='modificar-tipo'),
    path('hotel/<hid>/tipos-habitaciones/eliminar/<tid>/', views.eliminar_tipo, name='eliminar-tipo'),
]
