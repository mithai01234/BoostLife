from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Diet
from .serializers import DietSerializer

@permission_classes([IsAuthenticated])
class DietListByLevel(APIView):
    def get(self, request, *args, **kwargs):
        level = request.query_params.get('level', None)
        if level is not None:
            diets = Diet.objects.filter(level=level,status=True)
            serializer = DietSerializer(diets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Level query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TimeofFood
from .serializers import TimeofFoodSerializer

@permission_classes([IsAuthenticated])
class TimeofFoodListByTimeAndDiet(APIView):
    def get(self, request, *args, **kwargs):
        time = request.query_params.get('time', None)
        diet_id = request.query_params.get('diet_id', None)
        if time is not None and diet_id is not None:
            time_of_foods = TimeofFood.objects.filter(time=time, diet_id=diet_id,status=True)
            serializer = TimeofFoodSerializer(time_of_foods, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Both time and diet_id query parameters are required."}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DietVideo
from .serializers import DietVideoSerializer
from django.shortcuts import get_object_or_404

@permission_classes([IsAuthenticated])
class DietVideoByTimeofFood(APIView):
    def get(self, request, *args, **kwargs):
        timeoffood_id = request.query_params.get('timeoffood_id', None)
        if timeoffood_id is not None:
            diet_video = get_object_or_404(DietVideo, timeoffood_id__id=timeoffood_id,status=True)
            serializer = DietVideoSerializer(diet_video)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "timeoffood_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class DietVideoByVideoID(APIView):
    def get(self, request, *args, **kwargs):
        video_id = request.query_params.get('video_id', None)
        if video_id is not None:
            try:
                diet_video = DietVideo.objects.get(id=video_id)
                serializer = DietVideoSerializer(diet_video)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except DietVideo.DoesNotExist:
                return Response({"error": "DietVideo with this video_id does not exist."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "video_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
from .models import Ingredient, TimeofFood
from .serializers import IngredientSerializer

@permission_classes([IsAuthenticated])
class IngredientByTimeofFoodID(APIView):
    def get(self, request, *args, **kwargs):
        timeoffood_id = request.query_params.get('timeoffood_id', None)
        if timeoffood_id is not None:
            try:
                time_of_food = TimeofFood.objects.get(id=timeoffood_id)
                ingredients = time_of_food.ingredient_set.all()
                serializer = IngredientSerializer(ingredients, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except TimeofFood.DoesNotExist:
                return Response({"error": "TimeofFood with this timeoffood_id does not exist."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "timeoffood_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)