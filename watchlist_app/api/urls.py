# python imports
from django.urls import path, include

# project imports
from .views import MovieListAV, MovieDetailAV

urlpatterns = [
    path("", MovieListAV.as_view(), name="list-create"),
    path("<int:pk>/", MovieDetailAV.as_view(), name="retrieve-update-delete")
]
