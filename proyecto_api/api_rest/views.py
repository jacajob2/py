from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Producto

# Create your views here. 
#vista productos para 
class ProductoVista(View):
    def get(self,request):
        productos=list(Producto.objects.values())
        
        if len(productos)>0:
            datos={"mensaje":"Procesando Productos",'productos':productos}
        else:
            datos={"Mensaje":"Productos no encontrado..."}
        return JsonResponse(datos)

