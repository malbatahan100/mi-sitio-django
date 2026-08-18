from django.contrib import admin
from django.urls import path
from tareas.views import lista_de_tareas, completar_tarea
from donas.views import panel_ventas  # <--- Importamos tu nueva vista de donas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mis-tareas/', lista_de_tareas, name='lista_tareas'),
    path('completar/<int:tarea_id>/', completar_tarea, name='completar_tarea'),
    path('ventas-donas/', panel_ventas, name='panel_ventas'),  # <--- Nueva ruta del negocio
]
