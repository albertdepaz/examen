from rest_framework import serializers
from colegio.models import Asign


class AsignModelSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Asign
        fields = (
            'id',
            'curso',
            'alumno',
            'nota',
        )