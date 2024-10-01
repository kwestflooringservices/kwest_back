from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import render
from .models import Floor
from .serializers import FloorSerializer

# Create your views here.
class FloorListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        floors = Floor.objects.all()
        serializer = FloorSerializer(floors, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'floorname': request.data.get('floorname'),
            'floordesc': request.data.get('floordesc'),
            'manufacturer': request.data.get('manufacturer'),
            'onsale': request.data.get('onsale'),
            'price': request.data.get('price'),  # This field type is a guess.
            'inventory': request.data.get('inventory'),
            'floortype': request.data.get('floortype')
        }
        serializer = FloorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        floor = Floor.objects.get(pk = pk)
        serializer = FloorSerializer(instance = floor, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, pk, *args, **kwargs):
        floor = Floor.objects.get(pk = pk)
        floor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)