from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.TextField()
    descripción = models.TextField()
    
    def __str__(self):
        return self.nombre

class Comunicado(models.Model):
    NIVEL_CHOICES = [("GEN","General"),
                 ("PRE","Ciclo Preescolar",),
                 ("BAS","Ciclo Básico"),
                 ("MED","Ciclo Medio")]
    titulo = models.TextField()
    detalle = models.TextField()
    nivel = models.CharField(max_length=50, choices=NIVEL_CHOICES,default=NIVEL_CHOICES[0])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificación = models.DateTimeField()
    publicado_por = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo