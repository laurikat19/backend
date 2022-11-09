from django.db import models
from backend.utils.classes.BaseAbstractModel import BaseModel

class Asignatura(BaseModel):
    nombre = models.CharField('Nombre Asignatura', unique=True, max_length=150)
    codigo = models.CharField('Codigo Asignatura', unique=True, max_length=15)

    def __str__(self):
        return self.nombre
