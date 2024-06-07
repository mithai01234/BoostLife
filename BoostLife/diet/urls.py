
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('api/diets/', DietListByLevel.as_view(), name='diet_list_by_level'),
    path('api/timeoffoods/', TimeofFoodListByTimeAndDiet.as_view(), name='timeoffood_list_by_time_and_diet'),
    path('api/dietvideos/', DietVideoByTimeofFood.as_view(), name='dietvideo_by_timeoffood'),
    path('api/dietvideos/video/', DietVideoByVideoID.as_view(), name='dietvideo_by_video_id'),
    path('api/ingredients/', IngredientByTimeofFoodID.as_view(), name='ingredient_by_timeoffood_id'),

]
