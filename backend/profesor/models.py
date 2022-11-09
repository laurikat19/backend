from django.db import models
from backend.utils.classes.BaseAbstractModel import BaseModel
from django.core.validators import RegexValidator

class Profesor(BaseModel):
    nombre = models.CharField('Nombre Profesor', unique=True, max_length=255)
    correo = models.EmailField('Correo Profesor', unique=True, max_length=255)
    telefono_regex = RegexValidator(
        regex=r'\d{9,15}$',
        message="El número de teléfono debe ingresarse en el formato: 3004445566"
    )
    telefono = models.CharField('Telefono Profesor', validators=[telefono_regex], max_length=10, blank=False, null=False, unique=True)
    def __str__(self):
        return self.nombre
