from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    foto = models.ImageField(upload_to='departamentos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']


class Empleado(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='empleados/', blank=True, null=True)
    departamento = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, related_name='empleados'
    )

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    class Meta:
        ordering = ['apellidos', 'nombres']
