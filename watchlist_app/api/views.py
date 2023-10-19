# python imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# project imports
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer


@api_view(["GET", "POST"])
def list_create(request):
    if request.method == "GET":
        movies_queryset = Movie.objects.all()
        serializer = MovieSerializer(movies_queryset, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def retrieve_update_delete(request, pk):
    if request.method == "GET":
        try:
            movie = Movie.objects.get(pk=pk)
        except:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == "PUT":
        movie_instance = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
