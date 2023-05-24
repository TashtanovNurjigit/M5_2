from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .models import Movie


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = serializers.MovieListSerializers(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data

        movie = Movie.objects.create(
            director_id=data.get('director_id'),
            title=data.get('title'),
            description=data.get('description'),
            rate=data.get('rate')
        )
        movie.genres.set(data.get('genres'))
        return Response(data=serializers.MovieListSerializers(movie, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def movie_detail_api_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.MovieDetailSerializer(movie, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = request.data

        movie.director_id = data.get('director_id')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.rate = data.get('rate')
        movie.genres.set(data.get('genres'))

        movie.save()
        return Response(data=serializers.MovieDetailSerializer(movie, many=False).data, status=status.HTTP_200_OK)
