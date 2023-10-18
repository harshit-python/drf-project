from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse


def movie_list(request):
    movie_queryset = Movie.objects.all()
    data = {
        "movies": list(movie_queryset.values())
    }
    return JsonResponse(data)
