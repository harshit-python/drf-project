# python imports
from django.urls import path, include

# project imports
from .views import WatchListAV, WatchDetailAV, StreamPlatformListAV, StreamPlatformDetailAV

urlpatterns = [
    path("watchlist/", WatchListAV.as_view(), name="list-create-watchlist"),
    path("watchlist/<int:pk>/", WatchDetailAV.as_view(), name="retrieve-update-delete-watchlist"),
    path("stream/", StreamPlatformListAV.as_view(), name="list-create-streamplatform"),
    path("stream/<int:pk>/", StreamPlatformDetailAV.as_view(), name="retrieve-update-delete-streamplatform"),
]
