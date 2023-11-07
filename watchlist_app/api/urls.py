# python imports
from django.urls import path, include

# project imports
from .views import WatchListAV, WatchDetailAV, StreamPlatformListAV, StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path("watchlist/", WatchListAV.as_view(), name="list-create-watchlist"),
    path("watchlist/<int:pk>/", WatchDetailAV.as_view(), name="retrieve-update-delete-watchlist"),
    path("stream/", StreamPlatformListAV.as_view(), name="list-create-streamplatform"),
    path("stream/<int:pk>/", StreamPlatformDetailAV.as_view(), name="retrieve-update-delete-streamplatform"),
    path("review/", ReviewList.as_view(), name="list-review"),
    path("review/<int:pk>", ReviewDetail.as_view(), name="retrieve-review"),
]
