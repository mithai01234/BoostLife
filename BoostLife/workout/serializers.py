from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
# serializers.py

from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'name', 'video', 'time', 'repetition_time']  # Add other fields as needed
from rest_framework import serializers
from .models import WorkOutBanner

class WorkOutBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOutBanner
        fields = '__all__'

from rest_framework import serializers
from .models import Video

class RecVideoSerializer(serializers.ModelSerializer):
    workout_id = serializers.IntegerField(source='workout.id')
    workout_level = serializers.CharField(source='workout.level')
    workout_name = serializers.CharField(source='workout.name')
    workout_time = serializers.CharField(source='workout.time')
    workout_cal = serializers.CharField(source='workout.cal')
    workout_num_exercise = serializers.CharField(source='workout.num_exercise')
    workout_image = serializers.ImageField(source='workout.image')
    workout_status = serializers.BooleanField(source='workout.status')
    time_minutes = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            'id', 'workout_id', 'workout_level', 'workout_name', 'workout_time',
            'workout_cal', 'workout_num_exercise', 'workout_image', 'workout_status',
            'name', 'video', 'time', 'time_minutes', 'repetition_time', 'status', 'recommended'
        ]

    def get_time_minutes(self, obj):
        time_str = obj.time  # Assuming obj.time is a string in the format "HH:MM:SS"
        minutes = time_str.split(':')[1]  # Extract the minutes part
        return minutes