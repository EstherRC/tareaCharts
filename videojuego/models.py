from django.db import models


# Create your models here.

class Estudiante(models.Model):
    num_lista = models.IntegerField()
    grupo = models.CharField(max_length=60)
    progreso = models.IntegerField()

class Intentos(models.Model):
    fechaHora = models.CharField(max_length=60)
    completado = models.BooleanField()
    estudianteID = models.ForeignKey(Estudiante, related_name = "estudiante_id", on_delete=models.CASCADE)

class Juego(models.Model):
    mundo = models.IntegerField()
    nivel = models.IntegerField()