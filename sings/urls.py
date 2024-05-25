from django.urls import path
from .views import ListCategoryAPIView, ListRoadSingsAPIView, DetailRoadSingsAPIView

urlpatterns = [
    path('category-list/', ListCategoryAPIView.as_view(), name='category-list'),
    path('road-sings-list/', ListRoadSingsAPIView.as_view(), name='road-sings-list'),
    path('road-sings-detail/<int:pk>/', DetailRoadSingsAPIView.as_view(), name='road-sings-detail'),
]