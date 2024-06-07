from .views import *
from django.urls import path

urlpatterns = [
    path('api/article/', ImageInfoList.as_view(), name='image-info-list'),
    path('api/article/five/', ImageInfoListFive.as_view(), name='image-info-list'),

]