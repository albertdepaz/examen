from django.db import models
from utils.models import ColModel
from colegio.models.users import User
from colegio.models.cursos import Curso

class Asign(ColModel):
    alumno = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null= True)

    nota = models.IntegerField(blank=True)
    def __str__(self):
        return str(self.nota)