# python imports
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# project imports
from .views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    StreamPlatformVS,
    ReviewList,
    ReviewDetail,
    ReviewCreate
)

router = DefaultRouter()
router.register("stream", StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path("watchlist/", WatchListAV.as_view(), name="list-create-watchlist"),
    path("watchlist/<int:pk>/", WatchDetailAV.as_view(), name="retrieve-update-delete-watchlist"),
    path("", include(router.urls)),
    path("stream/<int:pk>/review-create/", ReviewCreate.as_view(), name="create-review"),
    path("stream/<int:pk>/review/", ReviewList.as_view(), name="list-review"),
    path("stream/review/<int:pk>/", ReviewDetail.as_view(), name="retrieve-update-delete-review"),
]
