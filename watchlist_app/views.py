# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse
#
#
# def filter_movies(request):
#     movies_queryset = Movie.objects.all()
#     data = {
#         "movies": list(movies_queryset.values())
#     }
#     return JsonResponse(data)
#
#
# def retrieve_movie(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         "name": movie.name,
#         "description": movie.description,
#         "active": movie.active
#     }
#     return JsonResponse(data)
