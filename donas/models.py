from django.db import models

# Create your models here.
from django.db import models

class VentaDona(models.Model):
    SABORES_CHOICES = [
        ('chocolate', 'Chocolate Glaseado'),
        ('fresa', 'Fresa con Chispas'),
        ('arequipe', 'Manjar / Arequipe'),
        ('clasica', 'Clásica de Azúcar'),
    ]

    sabor = models.CharField(max_length=50, choices=SABORES_CHOICES)
    cantidad = models.IntegerField(default=1)
    precio_total = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} dona(s) de {self.get_sabor_display()} (${self.precio_total})"
