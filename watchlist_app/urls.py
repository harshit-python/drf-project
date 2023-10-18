from django.urls import path, include
from .views import filter_movies, retrieve_movie

urlpatterns = [
    path("list/", filter_movies, name="filter-movies"),
    path("<int:pk>/", retrieve_movie, name="retrieve-movie")
]
