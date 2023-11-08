# python imports
from django.contrib import admin
from django.urls import path, include

# project imports

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("watchlist_app.api.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
