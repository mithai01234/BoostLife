from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.shortcuts import render, redirect, get_object_or_404
import json

# Create your views here.
@login_required(login_url='backend/login')
def customerlist(request):
    productapp=CustomUser.objects.all()

    context={
        'banform': productapp
    }
    return render(request,'backend/customerlist.html',context)
@login_required(login_url='backend/login')
def activate_customer(request, id):
    banner = get_object_or_404(CustomUser, id=id)
    banner.status = True
    banner.save()
    return redirect('customerlist')  # Redirect to your banner list view
@login_required(login_url='backend/login')
def deactivate_customer(request, id):
    banner = get_object_or_404(CustomUser, id=id)
    banner.status = False
    banner.save()
    return redirect('customerlist')  # Redirect to your banner list view


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    # permission_classes = [AllowAny]  # Allow access to all users

    def post(self, request):
        request_data = json.loads(request.body.decode('utf-8'))
        email = request_data.get('email')
        password = request_data.get('password', '')
       
        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.status:
            return Response({'error': 'Account is inactive'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        response_data = {
            'user_id': user.id,
            'goal': user.goal,
            'status': 'success',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data, status=status.HTTP_200_OK)
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer,ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# View for posting a new address
@permission_classes([IsAuthenticated])
class AddressCreateView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

# View for getting addresses by user_id
@permission_classes([IsAuthenticated])
class AddressListView(generics.ListAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            return Address.objects.filter(user_id=user_id)
        return Address.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"detail": "No addresses found for the given user_id."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    """
    API endpoint for user profiles.
    """

    def get(self, request):
        """
        Retrieve a specific user profile by user_id.
        """
        user_id = request.query_params.get('user_id')
        try:
            profile = CustomUser.objects.get(pk=user_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        Update a user profile.
        """
        user_id = request.data.get('user_id')
        try:
            profile = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Extract data from request
        name = request.data.get('name', "")
        email = request.data.get('email', "")
        bio = request.data.get('bio', "")
        profile_photo = request.FILES.get('profile_photo', "")  # Get the file from request.FILES
        new_password = request.data.get('password', "")

        # Update profile fields if provided
        if name is not None:
            profile.name = name
        if email is not None:
            profile.email = email
        if bio is not None:
            profile.bio = bio
        if profile_photo is not None:
            profile.profile_photo = profile_photo
        if new_password is not None:
            profile.set_password(new_password)

        profile.save()
        return Response({"success": "Profile updated successfully"}, status=status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404



class SignOutAPI(APIView):
    """
    API endpoint for user sign-out.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Retrieve the user_id from query parameters
        user_id = request.query_params.get('user_id')

        if not user_id:
            return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the user object
        user = get_object_or_404(CustomUser, id=user_id)

        # Perform any additional checks if needed (e.g., verify user's identity)

        # Perform the logout action
        logout(request)

        return Response({"message": "User successfully signed out."}, status=status.HTTP_200_OK)

class DeleteAccountAPI(APIView):
    """
    API endpoint for user account deletion.
    """
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        # Retrieve the user_id from query parameters
        user_id = request.query_params.get('user_id')

        if not user_id:
            return Response({"error": "user_id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the user object
        user = get_object_or_404(CustomUser, id=user_id)

        # Perform any additional checks if needed (e.g., verify user's identity)

        # Delete the user account
        user.delete()

        return Response({"message": "User account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
from django.contrib.auth.backends import BaseBackend


class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None