from rest_framework.serializers import ModelSerializer
from .models import Movie, Genre, Review


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = 'name'.split()


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = 'text stars'.split()


class MovieListSerializers(ModelSerializer):
    genres = GenreSerializer(many=True)
    filtered_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'preview', 'director_name', 'genres', 'filtered_reviews')


class MovieDetailSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
