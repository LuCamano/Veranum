from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import Hotel, Habitacion, TipoHabitacion
import os

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['nombre', 'direccion', 'telefono', 'comuna', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(
                Column(Field('nombre', id='nombre', placeholder='Nombre del hotel')),
                Column(Field('direccion', id='direccion', placeholder='Dirección del hotel')),
            ),
            Row(
                Column(Field('telefono', id='telefono', placeholder='Teléfono del hotel')),
                Column('comuna', id='comuna'),
            ),
            Field('imagen'),
            Submit('submit', 'Guardar')
        )

    def save(self, commit=True):
        imagen_vieja = None
        imagen_nueva = None
        try:
            oldHotel = self.Meta.model.objects.get(pk=self.instance.pk)
            imagen_vieja = oldHotel.imagen.path if oldHotel.imagen else None
            imagen_nueva = self.cleaned_data.get('imagen') if len(self.cleaned_data.get('imagen').name.split("/")) == 1 else None
        except:
            oldHotel = None
        super().save(commit)
        if imagen_nueva and imagen_vieja:
            if imagen_nueva.name != os.path.basename(imagen_vieja):
                if os.path.exists(imagen_vieja):
                    os.remove(imagen_vieja)

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = ['nombre', 'precio', 'cantidadCamas', 'cantidadBanos', 'servicios']

    def __init__(self, *args, **kwargs):
        hotel_id = kwargs.pop('hotel_id')
        super().__init__(*args, **kwargs)
        self.instance.hotel = Hotel.objects.get(pk=hotel_id)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(
                Column(Field('nombre', id='nombre')),
                Column(Field('precio', id='precio')),
            ),
            Row(
                Column(Field('cantidadCamas', id='cantidadCamas')),
                Column(Field('cantidadBanos', id='cantidadBanos')),
            ),
            Field('servicios', id='servicios'),
            Submit('submit', 'Guardar')
        )

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero', 'tipo', 'estado']

    def __init__(self, *args, **kwargs):
        hotel_id = kwargs.pop('hotel_id')
        super().__init__(*args, **kwargs)
        self.fields['tipo'].queryset = TipoHabitacion.objects.filter(hotel=hotel_id)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'needs-validation'
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(
                Column(Field('numero', id='numero')),
                Column(Field('tipo', id='tipo')),
            ),
            Field('estado', id='estado'),
            Submit('submit', 'Guardar')
        )