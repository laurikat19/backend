from django.db import models
from backend.utils.classes.BaseAbstractModel import BaseModel
from backend.asignatura.models import Asignatura
from backend.profesor.models import Profesor
class Clase(BaseModel):
    asignatura = models.OneToOneField(
        Asignatura,
        on_delete=models.CASCADE,
        related_name='asignatura',
    )
    profesor = models.OneToOneField(
        Profesor,
        on_delete=models.CASCADE,
        related_name='profesor',
    )
    salon = models.CharField('Salon Clase', max_length=255)
    Horario = models.TimeField('Horario clase')

    def __str__(self):
        return self.asignatura.nombre + ' - ' + self.salon
