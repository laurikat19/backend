from django.db import models
from backend.utils.classes.BaseAbstractModel import BaseModel
from backend.asignatura.models import Asignatura
from backend.profesor.models import Profesor
class Clase(BaseModel):
    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE,
        related_name='asignatura',
    )
    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.CASCADE,
        related_name='profesor',
    )
    salon = models.CharField('Salon Clase', max_length=255)
    horario = models.CharField('Horario clase', max_length=255)

    class Meta:
        unique_together = ('salon', 'horario',)
    def __str__(self):
        return self.asignatura.nombre + ' - ' + self.salon
