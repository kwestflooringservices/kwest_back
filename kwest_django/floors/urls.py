from django.urls import path,include
from .views import FloorListAPIView
urlpatterns = [
    path('api', FloorListAPIView.as_view(), name='floor_list'),
]