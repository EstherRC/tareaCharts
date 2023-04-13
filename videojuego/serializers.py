from rest_framework import serializers
from . models import Estudiante, Intentos, Juego

class IntentosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intentos
        fields = ('id','fechaHora', 'completado', 
        'estudianteID')

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id','num_lista','grupo','progreso')

class JuegoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Juego
        fields = ('id','mundo', 'nivel')
