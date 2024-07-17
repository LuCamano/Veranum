import django_filters
from .models import Hotel, Habitacion, TipoHabitacion

class HotelFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre')
    direccion = django_filters.CharFilter(lookup_expr='icontains', label='Dirección')

    class Meta:
        model = Hotel
        fields = {
            'comuna': ['exact'],
        }

class TipoHabitacionFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre')
    precio = django_filters.RangeFilter(label='Precio')
    cantidadCamas = django_filters.NumberFilter(label='Cantidad de camas')
    cantidadBanos = django_filters.NumberFilter(label='Cantidad de baños')

    class Meta:
        model = TipoHabitacion
        fields = ['servicios']

class HabitacionFilter(django_filters.FilterSet):
    numero = django_filters.NumberFilter(label='Número')
    tipo = django_filters.ModelChoiceFilter(label='Tipo de habitación')

    class Meta:
        model = Habitacion
        fields = {
            'estado': ['exact'],
        }
    
    def __init__(self, *args, **kwargs):
        hotel = kwargs.pop('hotel')
        super().__init__(*args, **kwargs)
        self.filters['tipo'].queryset = TipoHabitacion.objects.filter(hotel=hotel)
