from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta = models.CharField(max_length=300)
    