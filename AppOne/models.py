from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiate(models.Model):
    nombre= models.CharField('nombre', max_length=50)
    apellido= models.CharField('apellido', max_length=50)
    email = models.EmailField('email', max_length=254)
       
class Profesor(models.Model):
    nombre= models.CharField('nombre', max_length=50)
    apellido= models.CharField('apellido', max_length=50)
    email = models.EmailField('email', max_length=254)
    profesion = models.CharField('profesion', max_length=50)
    

class Entregable(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    fecha_de_entrega = models.DateField('fecha de entrega',)
    entregado = models.BooleanField()
           

