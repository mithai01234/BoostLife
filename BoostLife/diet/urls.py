
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views

urlpatterns = [
    path('api/diets/', DietListByLevel.as_view(), name='diet_list_by_level'),
    path('api/timeoffoods/', TimeofFoodListByTimeAndDiet.as_view(), name='timeoffood_list_by_time_and_diet'),
    path('api/dietvideos/', DietVideoByTimeofFood.as_view(), name='dietvideo_by_timeoffood'),
    path('api/dietvideos/video/', DietVideoByVideoID.as_view(), name='dietvideo_by_video_id'),
    path('api/ingredients/', IngredientByTimeofFoodID.as_view(), name='ingredient_by_timeoffood_id'),

    path('backend/diets/', views.diet_list, name='diet_list'),
    path('backend/diets/add/', views.diet_add, name='diet_add'),
    path('backend/diets/delete/<int:diet_id>/', views.diet_delete, name='diet_delete'),
    path('backend/diets/edit/<int:diet_id>/', views.diet_edit, name='diet_edit'),
    path('backend/diets/update/<int:diet_id>/', views.diet_update, name='diet_update'),
    path('backend/diets/activate/<int:diet_id>/', views.activate_diet, name='activate_diet'),
    path('backend/diets/deactivate/<int:diet_id>/', views.deactivate_diet, name='deactivate_diet'),

    # TimeofFood URLs
    path('backend/meal/', views.timeoffood_list, name='timeoffood_list'),
    path('backend/meal/add/', views.timeoffood_add, name='timeoffood_add'),
    path('backend/meal/delete/<int:timeoffood_id>/', views.timeoffood_delete, name='timeoffood_delete'),
    path('backend/meal/edit/<int:timeoffood_id>/', views.timeoffood_edit, name='timeoffood_edit'),
    path('backend/meal/update/<int:timeoffood_id>/', views.timeoffood_update, name='timeoffood_update'),
    path('backend/meal/activate/<int:timeoffood_id>/', views.activate_timeoffood, name='activate_timeoffood'),
    path('backend/meal/deactivate/<int:timeoffood_id>/', views.deactivate_timeoffood, name='deactivate_timeoffood'),

    # Ingredient URLs
    path('backend/ingredients/', views.ingredient_list, name='ingredient_list'),
    path('backend/ingredients/add/', views.ingredient_add, name='ingredient_add'),
    path('backend/ingredients/delete/<int:ingredient_id>/', views.ingredient_delete, name='ingredient_delete'),
    path('backend/ingredients/edit/<int:ingredient_id>/', views.ingredient_edit, name='ingredient_edit'),
    path('backend/ingredients/update/<int:ingredient_id>/', views.ingredient_update, name='ingredient_update'),
    path('backend/ingredients/activate/<int:ingredient_id>/', views.activate_ingredient, name='activate_ingredient'),
    path('backend/ingredients/deactivate/<int:ingredient_id>/', views.deactivate_ingredient, name='deactivate_ingredient'),

    path('backend/dietvideos/', views.dietvideo_list, name='dietvideo_list'),
    path('backend/dietvideos/add/', views.dietvideo_add, name='dietvideo_add'),
    path('backend/dietvideos/delete/<int:dietvideo_id>/', views.dietvideo_delete, name='dietvideo_delete'),
    path('backend/dietvideos/edit/<int:dietvideo_id>/', views.dietvideo_edit, name='dietvideo_edit'),
    path('backend/dietvideos/update/<int:dietvideo_id>/', views.dietvideo_update, name='dietvideo_update'),
    path('backend/dietvideos/activate/<int:dietvideo_id>/', views.activate_dietvideo, name='activate_dietvideo'),
    path('backend/dietvideos/deactivate/<int:dietvideo_id>/', views.deactivate_dietvideo, name='deactivate_dietvideo'),
    path('backend/dietvideo/view/<int:dietvideo_id>/', views.view_diet_video, name='view_diet_video'),
]
