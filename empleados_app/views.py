from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Departamento, Empleado
from .forms import DepartamentoForm, EmpleadoForm


def inicio(request):
    total_empleados = Empleado.objects.count()
    total_departamentos = Departamento.objects.count()
    return render(request, 'inicio.html', {
        'total_empleados': total_empleados,
        'total_departamentos': total_departamentos,
    })


# --- DEPARTAMENTOS ---

def departamento_lista(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/lista.html', {'departamentos': departamentos})


def departamento_crear(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento creado exitosamente.')
            return redirect('departamento_lista')
    else:
        form = DepartamentoForm()
    return render(request, 'departamentos/formulario.html', {'form': form, 'titulo': 'Crear Departamento'})


def departamento_editar(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, request.FILES, instance=departamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento actualizado exitosamente.')
            return redirect('departamento_lista')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'departamentos/formulario.html', {'form': form, 'titulo': 'Editar Departamento'})


def departamento_eliminar(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        departamento.delete()
        messages.success(request, 'Departamento eliminado exitosamente.')
        return redirect('departamento_lista')
    return render(request, 'departamentos/eliminar.html', {'departamento': departamento})


# --- EMPLEADOS ---

def empleado_lista(request):
    empleados = Empleado.objects.select_related('departamento').all()
    return render(request, 'empleados/lista.html', {'empleados': empleados})


def empleado_crear(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado creado exitosamente.')
            return redirect('empleado_lista')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/formulario.html', {'form': form, 'titulo': 'Crear Empleado'})


def empleado_editar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado exitosamente.')
            return redirect('empleado_lista')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/formulario.html', {'form': form, 'titulo': 'Editar Empleado'})


def empleado_eliminar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        messages.success(request, 'Empleado eliminado exitosamente.')
        return redirect('empleado_lista')
    return render(request, 'empleados/eliminar.html', {'empleado': empleado})
