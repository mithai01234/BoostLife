from .views import *
from django.urls import path

urlpatterns = [
    path('backend/customerlist/', customerlist, name="customerlist"),
    path('backend/customerlist/activate_product/<int:id>/', activate_customer, name='customerlist/activate_customer'),
    path('backend/customerlist/deactivate_product/<int:id>/', deactivate_customer,
         name='customerlist/deactivate_customer'),

    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='register'),

    path('api/addresses/', AddressListView.as_view(), name='address-list'),
    #http://127.0.0.1:8000/api/addresses/?user_id=4
    path('api/addresses/create/', AddressCreateView.as_view(), name='address-create'),

    path('api/profile/', ProfileAPI.as_view(), name='profile'),

    path('api/delete_account/', DeleteAccountAPI.as_view(), name='delete_account'),
    path('api/signout/', SignOutAPI.as_view(), name='signout'),
]