from rest_framework.serializers import ModelSerializer
from .models import Movie


class MovieListSerializers(ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'preview')


class MovieDetailSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
