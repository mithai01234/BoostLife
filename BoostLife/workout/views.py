from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout

@login_required(login_url='backend/login')
def workout_list(request):
    workouts = Workout.objects.all().order_by('-id')
    return render(request, 'backend/workout_list.html', {'workouts': workouts})

@login_required(login_url='backend/login')
def add_workout(request):
    if request.method == "POST":
        level = request.POST.get('level')
        name = request.POST.get('name')
        time = request.POST.get('time')
        cal = request.POST.get('cal')
        num_exercise = request.POST.get('num_exercise')
        image = request.FILES.get('image')

        Workout.objects.create(
            level=level,
            name=name,
            time=time,
            cal=cal,
            num_exercise=num_exercise,
            image=image
        )
        return redirect('workout_list')

    return render(request, 'backend/add_workout.html')

@login_required(login_url='backend/login')
def edit_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == "POST":
        workout.level = request.POST.get('level')
        workout.name = request.POST.get('name')
        workout.time = request.POST.get('time')
        workout.cal = request.POST.get('cal')
        workout.num_exercise = request.POST.get('num_exercise')
        if request.FILES.get('image'):
            workout.image = request.FILES.get('image')

        workout.save()
        return redirect('workout_list')

    return render(request, 'backend/edit_workout.html', {'workout': workout})

@login_required(login_url='backend/login')
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    workout.delete()
    return redirect('workout_list')

@login_required(login_url='backend/login')
def view_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    return render(request, 'backend/view_workout.html', {'workout': workout})

@login_required(login_url='backend/login')
def activate_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    workout.status = True  # Assuming there is a 'status' field in your model
    workout.save()
    return redirect('workout_list')

@login_required(login_url='backend/login')
def deactivate_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    workout.status = False  # Assuming there is a 'status' field in your model
    workout.save()
    return redirect('workout_list')

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Workout
from .serializers import WorkoutSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
@permission_classes([IsAuthenticated])
class WorkoutByLevelAPIView(APIView):
    def get(self, request):
        level = request.query_params.get('level', None)
        workout_id = request.query_params.get('id', None)

        if level is not None:
            workouts = Workout.objects.filter(level=level)
            serializer = WorkoutSerializer(workouts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if workout_id is not None:
            workout = get_object_or_404(Workout, id=workout_id)
            serializer = WorkoutSerializer(workout)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error": "Either 'level' or 'id' query parameter is required"},
                        status=status.HTTP_400_BAD_REQUEST)



from .models import Video, Workout

@login_required(login_url='backend/login')
def video_list(request):
    videos = Video.objects.all().order_by('-id')

    return render(request, 'backend/video_list.html', {'videos': videos})

@login_required(login_url='backend/login')
def add_video(request):
    workouts = Workout.objects.all()  # Get all workouts for the dropdown
    if request.method == "POST":
        workout_id = request.POST.get('workout')
        workout = get_object_or_404(Workout, id=workout_id)
        name = request.POST.get('name')
        video = request.FILES.get('video')
        type = request.POST.get('type')
        video_url = request.POST.get('video_url')
        time = request.POST.get('time')
        repetition_time = request.POST.get('repetition_time')
        recommended = request.POST.get('recommended') == 'on' if 'recommended' in request.POST else False

        if video or video_url:
            Video.objects.create(
                workout=workout,
                name=name,
                type=type,
                video=video,
                video_url=video_url,
                time=time,
                repetition_time=repetition_time,
                recommended=recommended
            )
            return redirect('video_list')

        return redirect('video_list')

    return render(request, 'backend/add_video.html', {'workouts': workouts})

@login_required(login_url='backend/login')
def edit_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    workouts = Workout.objects.all()  # Get all workouts for the dropdown
    if request.method == "POST":
        workout_id = request.POST.get('workout')
        video.workout = get_object_or_404(Workout, id=workout_id)
        video.name = request.POST.get('name')
        if request.FILES.get('video'):
            video.video = request.FILES.get('video')
        if request.POST.get('video_url'):
            video.video_url = request.POST.get('video_url')
        video.time = request.POST.get('time')
        video.repetition_time = request.POST.get('repetition_time')
        video.recommended = request.POST.get('recommended') == 'on' if 'recommended' in request.POST else False

        video.save()
        return redirect('video_list')

    return render(request, 'backend/edit_video.html', {'video': video, 'workouts': workouts})

@login_required(login_url='backend/login')
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    return redirect('video_list')

@login_required(login_url='backend/login')
def view_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'backend/view_video.html', {'video': video})
@login_required(login_url='backend/login')
def activate_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.status = True
    video.save()
    return redirect('video_list')

@login_required(login_url='backend/login')
def deactivate_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.status = False
    video.save()
    return redirect('video_list')


# views.py

from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Video

# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Video
from .serializers import VideoSerializer

# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Video
from .serializers import VideoSerializer
@permission_classes([IsAuthenticated])
class VideoDetailsView(APIView):
    def get(self, request):
        # Get the workout ID from query parameters
        workout_id = request.GET.get('workout_id')

        # Retrieve the video details based on the provided workout ID
        videos = Video.objects.filter(workout__id=workout_id)

        # Serialize the video data
        serializer = VideoSerializer(videos, many=True)
        for video_data in serializer.data:
            video_data['video'] = request.build_absolute_uri(video_data['video'])
        # Return the serialized video data as an array within JSON response
        return Response(serializer.data)

@permission_classes([IsAuthenticated])
class VideoDetailView(APIView):
    def get(self, request):
        # Get the video ID from query parameters
        video_id = request.GET.get('video_id')

        # Retrieve the video details based on the provided video ID
        video = get_object_or_404(Video, id=video_id)

        # Serialize the video data
        serializer = VideoSerializer(video)

        # Return the serialized video data with full video URL
        video_data = serializer.data
        video_data['video'] = request.build_absolute_uri(video_data['video'])

        return Response(video_data)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WorkOutBanner

@login_required(login_url='backend/login')
def workbanner_list(request):
    items = WorkOutBanner.objects.all()
    context = {
        'items': items
    }
    return render(request, 'backend/workbanner_list.html', context)

@login_required(login_url='backend/login')
def workadd_banner(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description', None) if 'description' in request.POST else None
        add_photo = request.FILES.get('item_photo')

        # Handling optional fields
        level = request.POST.get('level', None) if 'level' in request.POST else None
        workout_id = request.POST.get('workout_id', None) if 'workout_id' in request.POST else None

        # Create the item object
        item = WorkOutBanner.objects.create(
            title=title,
            description=description,
            add_photo=add_photo,
            status=True,
            level=level,
            workout_id=workout_id
        )
        return redirect('workbanner_list')

    # If the request method is not POST, render the form
    categories = Workout.objects.all()
    return render(request, 'backend/workadd_banner.html', {'categories': categories})

@login_required(login_url='backend/login')
def workactivate_add(request, add_id):
    item = get_object_or_404(WorkOutBanner, id=add_id)
    item.status = True
    item.save()
    return redirect('workbanner_list')

@login_required(login_url='backend/login')
def workdeactivate_add(request, add_id):
    item = get_object_or_404(WorkOutBanner, id=add_id)
    item.status = False
    item.save()
    return redirect('workbanner_list')

@login_required(login_url='backend/login')
def workdelete_add(request, add_id):
    item = get_object_or_404(WorkOutBanner, id=add_id)
    item.delete()
    return redirect('workbanner_list')

@login_required(login_url='backend/login')
def workview_add(request, add_id):
    item = get_object_or_404(WorkOutBanner, id=add_id)
    return render(request, 'backend/workview_banner.html', {'item': item})

@login_required(login_url='backend/login')
def workupdate_add(request, add_id):
    edit_item = get_object_or_404(WorkOutBanner, id=add_id)

    if request.method == "POST":
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
            add_photo = request.FILES.get('item_photo')
            category_id = request.POST.get('category')

            # Handling optional fields
            level = request.POST.get('level', None)
            workout_id = request.POST.get('workout_id', None)

            # Update the item object
            edit_item.title = title
            edit_item.description = description
            if add_photo:
                edit_item.add_photo = add_photo
            edit_item.category_id = category_id
            edit_item.level = level
            edit_item.workout_id = workout_id
            edit_item.save()

            return redirect('workbanner_list')  # Redirect to item list page after successful update
        except Exception as e:
            # If an error occurs during update, handle it here
            error_message = f'Error occurred while updating item: {e}'
            return render(request, 'backend/workedit_banner.html', {'item': edit_item, 'message': error_message})

    return render(request, 'backend/workedit_banner.html', {'item': edit_item})

@login_required(login_url='backend/login')
def workedit_add(request, add_id):
    sel_item = get_object_or_404(WorkOutBanner, id=add_id)
    all_items = WorkOutBanner.objects.all()
    categories = Workout.objects.all()

    context = {
        'all_items': all_items,
        'item': sel_item,
        'categories': categories
    }
    return render(request, 'backend/workedit_banner.html', context)

from rest_framework import generics
from .models import WorkOutBanner
from .serializers import WorkOutBannerSerializer,RecVideoSerializer

@permission_classes([IsAuthenticated])
class WorkOutBannerListByLevel(APIView):
    def get(self, request, *args, **kwargs):
        level = request.query_params.get('level', None)
        if level is not None:
            banner = WorkOutBanner.objects.filter(level=level, status=True).first()
            if banner:
                serializer = WorkOutBannerSerializer(banner)
                return Response(serializer.data)
        raise NotFound("Banner not found for the given level.")

@permission_classes([IsAuthenticated])
class WorkOutBannerListByWorkoutID(APIView):
    def get(self, request, *args, **kwargs):
        workout_id = request.query_params.get('workout_id', None)
        if workout_id is not None:
            banner = WorkOutBanner.objects.filter(workout_id=workout_id, status=True).first()
            if banner:
                serializer = WorkOutBannerSerializer(banner)
                return Response(serializer.data)
        raise NotFound("Banner not found for the given workout ID.")

@permission_classes([IsAuthenticated])
class RecommendedVideoList(generics.ListAPIView):
    queryset = Video.objects.filter(recommended=True,status=True)
    serializer_class = RecVideoSerializer
@permission_classes([IsAuthenticated])
class RecommendedVideoListFive(generics.ListAPIView):
    queryset = Video.objects.filter(recommended=True,status=True)[:5]
    serializer_class = RecVideoSerializer