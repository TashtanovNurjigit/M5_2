from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .models import Movie


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    serializer = serializers.MovieListSerializers(movies, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_api_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.MovieDetailSerializer(movie, many=False)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
