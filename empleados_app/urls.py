from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # Departamentos
    path('departamentos/', views.departamento_lista, name='departamento_lista'),
    path('departamentos/crear/', views.departamento_crear, name='departamento_crear'),
    path('departamentos/editar/<int:pk>/', views.departamento_editar, name='departamento_editar'),
    path('departamentos/eliminar/<int:pk>/', views.departamento_eliminar, name='departamento_eliminar'),
    # Empleados
    path('empleados/', views.empleado_lista, name='empleado_lista'),
    path('empleados/crear/', views.empleado_crear, name='empleado_crear'),
    path('empleados/editar/<int:pk>/', views.empleado_editar, name='empleado_editar'),
    path('empleados/eliminar/<int:pk>/', views.empleado_eliminar, name='empleado_eliminar'),
]
