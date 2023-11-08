# python imports
from rest_framework import serializers

# project imports
from watchlist_app.models import WatchList, StreamPlatform, Review


"""Model Serializers"""


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ("watchlist",)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    watchlist_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"

    # object level validator
    def validate(self, value):
        if value["title"] == value["storyline"]:
            raise serializers.ValidationError("Title and Storyline should be different!")
        return value

    # field level validator
    def title_length_validator(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist_platform = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"


"""Normal Serializers"""

#
# # field level validator
# def name_length_validator(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length_validator])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validate_data):
#         return Movie.objects.create(**validate_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance
#
#     # object level validator
#     def validate(self, value):
#         if value["name"] == value["description"]:
#             raise serializers.ValidationError("Title and Description should be different!")
#         return value
