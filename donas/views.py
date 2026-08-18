from django.shortcuts import render, redirect
from .models import VentaDona


def panel_ventas(request):
    if request.method == 'POST':
        # Capturamos los datos que el usuario escribe en el formulario HTML
        sabor_elegido = request.POST.get('sabor')
        cantidad_vendida = request.POST.get('cantidad')
        precio = request.POST.get('precio_total')

        # Guardamos la nueva venta en la base de datos
        VentaDona.objects.create(
            sabor=sabor_elegido,
            cantidad=cantidad_vendida,
            precio_total=precio
        )
        return redirect('panel_ventas')  # Recargamos la página para ver la actualización

    # Buscamos todas las ventas guardadas para mostrarlas abajo
    todas_las_ventas = VentaDona.objects.all()
    sabores = VentaDona.SABORES_CHOICES

    return render(request, 'donas/ventas.html', {
        'ventas': todas_las_ventas,
        'sabores': sabores
    })
