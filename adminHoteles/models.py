from django.db import models
from PIL import Image
import os
import uuid
# Create your models here.
class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Hotel(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    direccion = models.CharField("Dirección", max_length=100)
    telefono = models.CharField("Teléfono", max_length=12)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    imagen = models.ImageField("Imagen", upload_to="hoteles", null=True, blank=True)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"

    @property
    def cantHabitaciones(self):
        return Habitacion.objects.filter(tipo__hotel=self).count()

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagen and os.path.exists(self.imagen.path):
            with Image.open(self.imagen.path) as img:
                ancho, alto = img.size

                if ancho > alto:
                    # La imagen es mas ancha que alta
                    nuevo_alto = 1280
                    nuevo_ancho = int((ancho/alto) * nuevo_alto)
                    img = img.resize((nuevo_ancho, nuevo_alto))
                    img.save(self.imagen.path)
                elif alto > ancho:
                    # La imagen es mas alta que ancha
                    nuevo_ancho = 1280
                    nuevo_alto = int((alto/ancho) * nuevo_ancho)
                    img = img.resize((nuevo_ancho, nuevo_alto))
                    img.save(self.imagen.path)
                else:
                    # La imagen es cuadrada
                    img.thumbnail((300, 300))
                    img.save(self.imagen.path)

            # El recorte de la imagen final
            with Image.open(self.imagen.path) as img:
                ancho, alto = img.size

                if ancho > alto:
                    left = (ancho - alto) / 2
                    top = 0
                    right = (ancho + alto) / 2
                    bottom = alto

                else:
                    left = 0
                    top = (alto - ancho) / 2
                    right = ancho
                    bottom = (alto + ancho) / 2

                img = img.crop((left, top, right, bottom))
                img.save(self.imagen.path)

    def delete(self, *args, **kwargs):
        if self.imagen and os.path.exists(self.imagen.path):
            os.remove(self.imagen.path)
        return super().delete(*args, **kwargs)

class TipoHabitacion(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nombre = models.CharField("Nombre", max_length=50)
    precio = models.PositiveIntegerField("Precio por noche")
    cantidadCamas = models.PositiveIntegerField("Cantidad de camas")
    cantidadBanos = models.PositiveIntegerField("Cantidad de baños")
    servicios = models.ManyToManyField("adminHoteles.ServicioAdicional", verbose_name="Servicios Adicionales", help_text="CTRL + Click para seleccionar varios", blank=True)
    hotel = models.ForeignKey("adminHoteles.Hotel", verbose_name="Hotel", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de Habitación"
        verbose_name_plural = "Tipos de Habitaciones"

class Habitacion(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    numero = models.PositiveIntegerField("Número")
    estado = models.CharField("Estado", max_length=50, default="Disponible", choices=[("Disponible", "Disponible"), ("Ocupada", "Ocupada"), ("Mantenimiento", "Mantenimiento"), ("Reservada", "Reservada"), ("No Disponible", "No Disponible")])
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.numero} - {self.tipo.nombre}"
    
    @property
    def hotel(self):
        return self.tipo.hotel
    
    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"

    def save(self, *args, **kwargs):
        existentes = Habitacion.objects.filter(numero=self.numero)
        for habitacion in existentes:
            if habitacion.id != self.id and habitacion.hotel == self.hotel:
                raise Exception("Ya existe una habitación con ese número en el hotel seleccionado")
        return super().save(*args, **kwargs)

class ServicioAdicional(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Servicio Adicional"
        verbose_name_plural = "Servicios Adicionales"