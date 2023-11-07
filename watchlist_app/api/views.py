# python imports
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins

# project imports
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StreamPlatformListAV(APIView):

    def get(self, request):
        streamplatform_objects = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streamplatform_objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            streamplatform_object = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({"error": "Stream Platform not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(streamplatform_object)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            streamplatform_object = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({"error": "Stream Platform not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(data=request.data, instance=streamplatform_object)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            streamplatform_object = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({"error": "Stream Platform not found"}, status=status.HTTP_404_NOT_FOUND)
        streamplatform_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        watchlist_objects = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist_objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):

    def get(self, request, pk):
        try:
            watchlist_object = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchlist_object)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            watchlist_object = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchlist_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            watchlist_object = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error": "WatchList not found"}, status=status.HTTP_404_NOT_FOUND)
        watchlist_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def list_create(request):
#     if request.method == "GET":
#         movies_queryset = Movie.objects.all()
#         serializer = MovieSerializer(movies_queryset, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def retrieve_update_delete(request, pk):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except:
#             return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == "PUT":
#         movie_instance = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == "DELETE":
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
