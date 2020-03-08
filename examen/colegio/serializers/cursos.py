from rest_framework import serializers
from colegio.models import Curso


class CursosModelSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Curso
        fields = (
            'id',
            'profesor',
            'nombre_curso',
            'descripcion',
        )
