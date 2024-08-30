from django.contrib import admin

# Register your models here.
#importar la estructura del modelo
from .models import Producto
#registrar la clase en el site
admin.site.register(Producto)
