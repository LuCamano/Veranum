from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HabitacionForm, TipoHabitacionForm, HotelForm
from .models import Habitacion, TipoHabitacion, Hotel
# Create your views here.
def listado_hoteles(request):
    hoteles = Hotel.objects.all()
    context = {
        'hoteles': hoteles
    }
    return render(request, 'adminHoteles/listado hoteles.html', context)

def agregar_hotel(request):
    form = HotelForm()
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hotel agregado correctamente')
            return redirect('listado_hoteles')
        else:
            messages.error(request, 'Error al agregar el hotel')
            return redirect('agregar-hotel')
    context = {
        'form': form,
        'titulo': 'Agregar Hotel'
    }
    return render(request, 'adminHoteles/formulario.html', context)

def eliminar_hotel(request, id):
    hotel = Hotel.objects.get(pk=id)
    hotel.delete()
    messages.success(request, 'Hotel eliminado correctamente')
    return redirect('listado_hoteles')

def modificar_hotel(request, id):
    hotel = Hotel.objects.get(pk=id)
    form = HotelForm(instance=hotel)
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hotel modificado correctamente')
            return redirect('listado_hoteles')
        else:
            messages.error(request, 'Error al modificar el hotel')
            return redirect('modificar-hotel', id=id)
    context = {
        'form': form,
        'titulo': 'Modificar Hotel'
    }
    return render(request, 'adminHoteles/formulario.html', context)

def vista_hotel(request, id):
    hotel = Hotel.objects.get(pk=id)
    context = {
        'hotel': hotel
    }
    return render(request, 'adminHoteles/vista hotel.html', context)

def listado_habitaciones(request, id):
    hotel = Hotel.objects.get(pk=id)
    habitaciones = Habitacion.objects.filter(tipo__hotel=hotel)
    context = {
        'hotel': hotel,
        'habitaciones': habitaciones
    }
    return render(request, 'adminHoteles/listado habitaciones.html', context)

def agregar_habitacion(request, id):
    form = HabitacionForm(hotel_id=id)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, hotel_id=id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Habitacion agregada correctamente')
            return redirect('habitaciones', id=id)
        else:
            messages.error(request, 'Error al agregar la habitacion')
            return redirect('agregar-habitacion', id=id)
    context = {
        'form': form,
        'titulo': 'Agregar Habitacion'
    }
    return render(request, 'adminHoteles/formulario.html', context)

def modificar_habitacion(request, id, hid):
    habitacion = Habitacion.objects.get(pk=hid)
    form = HabitacionForm(instance=habitacion, hotel_id=id)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, instance=habitacion, hotel_id=id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Habitacion modificada correctamente')
            return redirect('habitaciones', id=id)
        else:
            messages.error(request, 'Error al modificar la habitacion')
            return redirect('modificar-habitacion', id=id, hid=hid)
    context = {
        'form': form,
        'titulo': 'Modificar Habitacion'
    }
    return render(request, 'adminHoteles/formulario.html', context)

def eliminar_habitacion(request, id, hid):
    habitacion = Habitacion.objects.get(pk=hid)
    habitacion.delete()
    messages.success(request, 'Habitacion eliminada correctamente')
    return redirect('habitaciones', id=id)

def tipo_habitaciones(request, id):
    hotel = Hotel.objects.get(pk=id)
    tipos = TipoHabitacion.objects.filter(hotel=hotel)
    context = {
        'hotel': hotel,
        'tipos': tipos,
    }
    return render(request, 'adminHoteles/tipos habitaciones.html', context)

def agregar_tipo(request, hid):
    form = TipoHabitacionForm(hotel_id=hid)
    if request.method == 'POST':
        form = TipoHabitacionForm(request.POST, hotel_id=hid)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de habitacion agregado correctamente')
            return redirect('tipo-habitaciones', id=hid)
        else:
            messages.error(request, 'Error al agregar el tipo de habitacion')
            return redirect('agregar-tipo', hid=hid)
    context = {
        'form': form,
        'titulo': 'Agregar Tipo de Habitacion'
    }
    return render(request, 'adminHoteles/formulario.html', context)

def modificar_tipo(request, hid, tid):
    tipo = TipoHabitacion.objects.get(pk=tid)
    form = TipoHabitacionForm(instance=tipo, hotel_id=hid)
    if request.method == 'POST':
        form = TipoHabitacionForm(request.POST, instance=tipo, hotel_id=hid)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de habitacion modificado correctamente')
            return redirect('tipo-habitaciones', id=hid)
        else:
            messages.error(request, 'Error al modificar el tipo de habitacion')
            return redirect('modificar-tipo', hid=hid, tid=tid)
    context = {
        'form': form,
        'titulo': 'Modificar Tipo de Habitacion'
    }
    return render(request, 'adminHoteles/formulario.html', context)

def eliminar_tipo(request, hid, tid):
    tipo = TipoHabitacion.objects.get(pk=tid)
    tipo.delete()
    messages.success(request, 'Tipo de habitacion eliminado correctamente')
    return redirect('tipo-habitaciones', id=hid)