#Django rest_framework
from rest_framework import mixins, viewsets
#Serializers
from colegio.serializers.cursos import CursosModelSerializer
#Models
from colegio.models import Curso


class CursoViewSet(viewsets.ModelViewSet):
    """Curso view set."""
    queryset = Curso.objects.all()
    serializer_class = CursosModelSerializer
