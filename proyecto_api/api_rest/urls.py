from django.urls import path

from .views import ProductoVista
urlpatterns=[
    path('productos',ProductoVista.as_view(),name="productos_lista")
]