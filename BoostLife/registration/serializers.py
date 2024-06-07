from rest_framework import serializers
from .models import CustomUser

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'phone_number', 'email', 'password', 'gender', 'age', 'height', 'weight', 'activity_level', 'goal']
        extra_kwargs = {
            'password': {'write_only': True},  # Password should be write only
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'required': False},
            'phone_number': {'required': False},
            'email': {'required': False},
        }
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'bio','profile_photo']
        extra_kwargs = {
            'password': {'required': False},  # Allow password to be optional
            'email': {'required': False},  # Make email optional
            'bio': {'required': False},
            'name': {'required': False},
            # Make bio optional
            'profile_photo': {'required': False},
        }