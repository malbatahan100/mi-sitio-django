import os
import sys
from django.core.wsgi import get_wsgi_application

# Ajuste de rutas estándar para Vercel
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_sitio.settings')

application = get_wsgi_application()
app = application
