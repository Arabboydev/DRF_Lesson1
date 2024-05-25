from rest_framework import serializers
from .models import CategorySings, RoadSings


class CategorySingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySings
        fields = "__all__"


class RoadSingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSings
        fields = "__all__"


class RoadSingsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSings
        fields = ['id', 'category', 'name', 'image', 'video', 'audio', 'dock']