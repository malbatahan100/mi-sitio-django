from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404 # <--- Asegúrate que termine en _404 con O de oso, no con cero 0
from .models import Tarea

def lista_de_tareas(request):
    todas_las_tareas = Tarea.objects.all()
    return render(request, 'tareas/lista.html', {'tareas': todas_las_tareas})

def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('lista_tareas')
