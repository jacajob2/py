from django.db import models

# Create your models here.
class Producto(models.Model):
    
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    #nuevo campo
    cantidad=models.IntegerField()