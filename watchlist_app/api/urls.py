# python imports
from django.urls import path, include

# project imports
from .views import list_create, retrieve_update_delete

urlpatterns = [
    path("", list_create, name="list-create"),
    path("<int:pk>/", retrieve_update_delete, name="retrieve-update-delete")
]
