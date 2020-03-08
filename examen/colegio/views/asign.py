#Django rest_framework
from rest_framework import mixins, viewsets
#Serializers
from colegio.serializers.asign import AsignModelSerializer
#Models
from colegio.models import Asign


class AsignViewSet(viewsets.ModelViewSet):
    """Curso view set."""
    queryset = Asign.objects.all()
    serializer_class = AsignModelSerializer
