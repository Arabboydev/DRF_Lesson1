from django.shortcuts import render, get_object_or_404
from .serializs import CategorySingsSerializer, RoadSingsSerializer, RoadSingsDetailSerializer
from .models import CategorySings, RoadSings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ListCategoryAPIView(APIView):
    def get(self, request):
        category = CategorySings.objects.all()
        serializer = CategorySingsSerializer(category, many=True)
        serializer_data = {
            'category_id': serializer.data,
            'status': "success",
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class ListRoadSingsAPIView(APIView):
    def get(self, request):
        model = RoadSings.objects.all()
        serializer = RoadSingsSerializer(model, many=True)
        serializer_data = {
            "model": serializer.data,
            "status": "success",
            'status_code': status.HTTP_200_OK,
        }
        return Response(serializer_data)


class DetailRoadSingsAPIView(APIView):
    def get(self, request, pk):
        model = get_object_or_404(RoadSings, pk=pk)
        serializer = RoadSingsDetailSerializer(model)
        serializer_data = {
            "model": serializer.data,
            "status": "success",
            'status_code': status.HTTP_200_OK,
        }
        return Response(serializer_data)