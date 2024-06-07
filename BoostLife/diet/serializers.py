from rest_framework import serializers
from .models import Diet

class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'
from rest_framework import serializers
from .models import TimeofFood

class TimeofFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeofFood
        fields = '__all__'
from rest_framework import serializers
from .models import DietVideo

class DietVideoSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = DietVideo
        fields = '__all__'

    def get_video(self, obj):
        request = self.context.get('request')
        domain = "http://192.168.29.213:8000"
        if request:
            return request.build_absolute_uri(obj.video.url)
        return f"{domain}{obj.video.url}"


from rest_framework import serializers
from .models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
