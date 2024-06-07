from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Article
from .serializers import ImageInfoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
@permission_classes([IsAuthenticated])
class ImageInfoList(generics.ListAPIView):
    queryset = Article.objects.filter(status=True).order_by('-id')
    serializer_class = ImageInfoSerializer
@permission_classes([IsAuthenticated])
class ImageInfoListFive(generics.ListAPIView):
    queryset = Article.objects.filter(status=True).order_by('-id')[:5]
    serializer_class = ImageInfoSerializer
