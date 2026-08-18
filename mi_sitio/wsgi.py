import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

# Ajuste de rutas necesario para que Vercel encuentre tu proyecto
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_sitio.settings')

application = get_wsgi_application()
app = application

# Truco definitivo: Ejecuta las migraciones en Supabase al arrancar
try:
    print("Iniciando migraciones automáticas en Supabase...")
    call_command('migrate', interactive=False)
    print("¡Migraciones completadas con éxito!")
except Exception as e:
    print(f"Aviso en migración: {e}")
