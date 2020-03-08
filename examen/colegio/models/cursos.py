from django.db import models
from utils.models import ColModel
from colegio.models.users import User
class Curso(ColModel):
    nombre_curso = models.CharField(max_length=500, blank=True)
    profesor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return str(self.nombre_curso)
