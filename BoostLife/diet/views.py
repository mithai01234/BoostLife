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





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Diet, TimeofFood, Ingredient

@login_required(login_url='backend/login')
def diet_list(request):
    diets = Diet.objects.all()
    context = {
        'diets': diets
    }
    return render(request, 'backend/diet_list.html', context)

@login_required(login_url='backend/login')
def diet_add(request):
    if request.method == "POST":
        diet = Diet()
        diet.name = request.POST.get('name')
        diet.carbs = 'carbs' in request.POST
        diet.protein = 'protein' in request.POST
        diet.fat = 'fat' in request.POST
        diet.number_of_intake = request.POST.get('number_of_intake')
        diet.level = request.POST.get('level')
        diet.image = request.FILES.get('image')
        diet.save()
        return redirect('diet_list')
    return render(request, 'backend/diet_add.html')

@login_required(login_url='backend/login')
def diet_delete(request, diet_id):
    diet = get_object_or_404(Diet, id=diet_id)
    diet.delete()
    return redirect('diet_list')

@login_required(login_url='backend/login')
def diet_edit(request, diet_id):
    diet = get_object_or_404(Diet, id=diet_id)
    context = {
        'diet': diet
    }
    return render(request, 'backend/diet_edit.html', context)

@login_required(login_url='backend/login')
def diet_update(request, diet_id):
    diet = get_object_or_404(Diet, id=diet_id)
    if request.method == "POST":
        diet.name = request.POST.get('name')
        diet.carbs = 'carbs' in request.POST
        diet.protein = 'protein' in request.POST
        diet.fat = 'fat' in request.POST
        diet.number_of_intake = request.POST.get('number_of_intake')
        diet.level = request.POST.get('level')
        if request.FILES.get('image'):
            diet.image = request.FILES.get('image')
        diet.save()
        return redirect('diet_list')
    return render(request, 'backend/diet_edit.html', {'diet': diet})

@login_required(login_url='backend/login')
def activate_diet(request, diet_id):
    diet = get_object_or_404(Diet, id=diet_id)
    diet.status = True
    diet.save()
    return redirect('diet_list')

@login_required(login_url='backend/login')
def deactivate_diet(request, diet_id):
    diet = get_object_or_404(Diet, id=diet_id)
    diet.status = False
    diet.save()
    return redirect('diet_list')




@login_required(login_url='backend/login')
def timeoffood_list(request):
    timeoffoods = TimeofFood.objects.all()
    context = {
        'timeoffoods': timeoffoods
    }
    return render(request, 'backend/timeoffood_list.html', context)

@login_required(login_url='backend/login')
def timeoffood_add(request):
    diets = Diet.objects.all()  # Fetch diets to select in the form
    if request.method == "POST":
        timeoffood = TimeofFood()
        timeoffood.name = request.POST.get('name')
        timeoffood.number_of_cup = request.POST.get('number_of_cup')
        timeoffood.number_of_gram = request.POST.get('number_of_gram')
        timeoffood.calories = request.POST.get('calories')
        timeoffood.time = request.POST.get('time')
        timeoffood.diet_id = Diet.objects.get(id=request.POST.get('diet_id'))
        timeoffood.image = request.FILES.get('image')
        timeoffood.save()
        return redirect('timeoffood_list')
    return render(request, 'backend/timeoffood_add.html', {'diets': diets})

@login_required(login_url='backend/login')
def timeoffood_delete(request, timeoffood_id):
    timeoffood = get_object_or_404(TimeofFood, id=timeoffood_id)
    timeoffood.delete()
    return redirect('timeoffood_list')

@login_required(login_url='backend/login')
def timeoffood_edit(request, timeoffood_id):
    timeoffood = get_object_or_404(TimeofFood, id=timeoffood_id)
    diets = Diet.objects.all()  # Fetch diets to select in the form
    context = {
        'timeoffood': timeoffood,
        'diets': diets
    }
    return render(request, 'backend/timeoffood_edit.html', context)

@login_required(login_url='backend/login')
def timeoffood_update(request, timeoffood_id):
    timeoffood = get_object_or_404(TimeofFood, id=timeoffood_id)
    if request.method == "POST":
        timeoffood.name = request.POST.get('name')
        timeoffood.number_of_cup = request.POST.get('number_of_cup')
        timeoffood.number_of_gram = request.POST.get('number_of_gram')
        timeoffood.calories = request.POST.get('calories')
        timeoffood.time = request.POST.get('time')
        timeoffood.diet_id = Diet.objects.get(id=request.POST.get('diet_id'))
        if request.FILES.get('image'):
            timeoffood.image = request.FILES.get('image')
        timeoffood.save()
        return redirect('timeoffood_list')
    return render(request, 'backend/timeoffood_edit.html', {'timeoffood': timeoffood, 'diets': Diet.objects.all()})

@login_required(login_url='backend/login')
def activate_timeoffood(request, timeoffood_id):
    timeoffood = get_object_or_404(TimeofFood, id=timeoffood_id)
    timeoffood.status = True
    timeoffood.save()
    return redirect('timeoffood_list')

@login_required(login_url='backend/login')
def deactivate_timeoffood(request, timeoffood_id):
    timeoffood = get_object_or_404(TimeofFood, id=timeoffood_id)
    timeoffood.status = False
    timeoffood.save()
    return redirect('timeoffood_list')




@login_required(login_url='backend/login')
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    context = {
        'ingredients': ingredients
    }
    return render(request, 'backend/ingredient_list.html', context)

@login_required(login_url='backend/login')
def ingredient_add(request):
    timeoffoods = TimeofFood.objects.all()  # Fetch timeoffoods to select in the form
    if request.method == "POST":
        ingredient = Ingredient()
        ingredient.name = request.POST.get('name')
        ingredient.measurement = request.POST.get('measurement')
        ingredient.timeoffood_id = TimeofFood.objects.get(id=request.POST.get('timeoffood_id'))
        ingredient.image = request.FILES.get('image')
        ingredient.save()
        return redirect('ingredient_list')
    return render(request, 'backend/ingredient_add.html', {'timeoffoods': timeoffoods})

@login_required(login_url='backend/login')
def ingredient_delete(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    ingredient.delete()
    return redirect('ingredient_list')

@login_required(login_url='backend/login')
def ingredient_edit(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    timeoffoods = TimeofFood.objects.all()  # Fetch timeoffoods to select in the form
    context = {
        'ingredient': ingredient,
        'timeoffoods': timeoffoods
    }
    return render(request, 'backend/ingredient_edit.html', context)

@login_required(login_url='backend/login')
def ingredient_update(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == "POST":
        ingredient.name = request.POST.get('name')
        ingredient.measurement = request.POST.get('measurement')
        ingredient.timeoffood_id = TimeofFood.objects.get(id=request.POST.get('timeoffood_id'))
        if request.FILES.get('image'):
            ingredient.image = request.FILES.get('image')
        ingredient.save()
        return redirect('ingredient_list')
    return render(request, 'backend/ingredient_edit.html', {'ingredient': ingredient, 'timeoffoods': TimeofFood.objects.all()})

@login_required(login_url='backend/login')
def activate_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    ingredient.status = True
    ingredient.save()
    return redirect('ingredient_list')

@login_required(login_url='backend/login')
def deactivate_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    ingredient.status = False
    ingredient.save()
    return redirect('ingredient_list')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Diet, TimeofFood, Ingredient, DietVideo

@login_required(login_url='backend/login')
def dietvideo_list(request):
    dietvideos = DietVideo.objects.all()
    context = {
        'dietvideos': dietvideos
    }
    return render(request, 'backend/dietvideo_list.html', context)

@login_required(login_url='backend/login')
def dietvideo_add(request):
    timeoffoods = TimeofFood.objects.all()  # Fetch timeoffoods to select in the form
    if request.method == "POST":
        dietvideo = DietVideo()
        dietvideo.preptime = request.POST.get('preptime')
        dietvideo.carbs = request.POST.get('carbs')
        dietvideo.fat = request.POST.get('fat')
        dietvideo.protein = request.POST.get('protein')
        dietvideo.type = request.POST.get('type')

        dietvideo.precautions = request.POST.get('precautions')
        dietvideo.video = request.FILES.get('video') if request.FILES.get('video') else dietvideo.video
        dietvideo.video_url = request.POST.get('video_url') if request.POST.get('video_url') else dietvideo.video_url
        dietvideo.timeoffood_id = TimeofFood.objects.get(id=request.POST.get('timeoffood_id'))
        dietvideo.save()
        return redirect('dietvideo_list')
    return render(request, 'backend/dietvideo_add.html', {'timeoffoods': timeoffoods})

@login_required(login_url='backend/login')
def dietvideo_delete(request, dietvideo_id):
    dietvideo = get_object_or_404(DietVideo, id=dietvideo_id)
    dietvideo.delete()
    return redirect('dietvideo_list')

@login_required(login_url='backend/login')
def dietvideo_edit(request, dietvideo_id):
    dietvideo = get_object_or_404(DietVideo, id=dietvideo_id)
    timeoffoods = TimeofFood.objects.all()  # Fetch timeoffoods to select in the form
    context = {
        'dietvideo': dietvideo,
        'timeoffoods': timeoffoods
    }
    return render(request, 'backend/dietvideo_edit.html', context)

@login_required(login_url='backend/login')
def dietvideo_update(request, dietvideo_id):
    dietvideo = get_object_or_404(DietVideo, id=dietvideo_id)
    if request.method == "POST":
        dietvideo.preptime = request.POST.get('preptime')
        dietvideo.carbs = request.POST.get('carbs')
        dietvideo.fat = request.POST.get('fat')
        dietvideo.protein = request.POST.get('protein')
        dietvideo.precautions = request.POST.get('precautions')
        if request.FILES.get('video'):
            dietvideo.video = request.FILES.get('video')
        if request.POST.get('video_url'):
            dietvideo.video_url = request.POST.get('video_url')
        dietvideo.timeoffood_id = TimeofFood.objects.get(id=request.POST.get('timeoffood_id'))
        dietvideo.save()
        return redirect('dietvideo_list')
    return render(request, 'backend/dietvideo_edit.html', {'dietvideo': dietvideo, 'timeoffoods': TimeofFood.objects.all()})

@login_required(login_url='backend/login')
def activate_dietvideo(request, dietvideo_id):
    dietvideo = get_object_or_404(DietVideo, id=dietvideo_id)
    dietvideo.status = True
    dietvideo.save()
    return redirect('dietvideo_list')

@login_required(login_url='backend/login')
def deactivate_dietvideo(request, dietvideo_id):
    dietvideo = get_object_or_404(DietVideo, id=dietvideo_id)
    dietvideo.status = False
    dietvideo.save()
    return redirect('dietvideo_list')
@login_required(login_url='backend/login')
def view_diet_video(request, dietvideo_id):
    dietvideo = get_object_or_404(DietVideo, pk=dietvideo_id)
    context = {
        'dietvideo': dietvideo
    }
    return render(request, 'backend/view_diet_video.html', context)

