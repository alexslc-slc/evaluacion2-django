from django.contrib import admin
from .models import Departamento, Empleado


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion')


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cargo', 'departamento')
    list_filter = ('departamento',)
