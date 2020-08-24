from .models import Pelicula
from rest_framework import serializers
from .models import Pelicula, PeliculaFavorita


class PeliculaSerializer(serializers.ModelSerializer): # transformar a formato JSON
  class Meta:
    model = Pelicula
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'


class PeliculaFavoritaSerializer(serializers.ModelSerializer):
  
  pelicula = PeliculaSerializer()

  class Meta:
    model = PeliculaFavorita
    fields = ['pelicula']