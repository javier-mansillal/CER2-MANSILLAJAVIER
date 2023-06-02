from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.TextField()
    descripción = models.TextField()

class Comunicado(models.Model):
    titulo = models.TextField()
    detalle = models.TextField()
    nivel = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificación = models.DateTimeField()
    publicado_por = models.CharField(max_length=200)
