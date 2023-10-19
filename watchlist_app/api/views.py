# python imports
from rest_framework.response import Response
from rest_framework.decorators import api_view

# project imports
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer


@api_view()
def filter_movies(request):
    movies_queryset = Movie.objects.all()
    serializer = MovieSerializer(movies_queryset, many=True)
    return Response(serializer.data)


@api_view()
def retrieve_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)