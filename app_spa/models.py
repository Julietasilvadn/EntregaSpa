from django.db import models

class Persona(models.Model):

    nombre=models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)
    dni= models.IntegerField()
    email= models.EmailField()
    contraseña= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} - Email: {self.email} - Contraseña: {self.contraseña}"

class Mascota(models.Model):
    nombre= models.CharField(max_length=30)
    raza= models.CharField(max_length=30)
    edad= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Raza: {self.raza} - Edad: {self.edad}"


class Reserva(models.Model):
    dueño= models.CharField(max_length=40)
    mascota= models.CharField(max_length=40)
    fecha= models.DateTimeField()

    def __str__(self):
        return f"Dueño: {self.dueño} - Mascota: {self.mascota} - Fecha: {self.fecha}"