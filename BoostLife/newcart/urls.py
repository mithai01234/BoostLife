from django.urls import path
from .views import *
urlpatterns = [
    path('backend/chargeapp/', charge, name="chargeapp"),
    path('backend/chargeadd/', chargeadd, name="chargeadd"),
    path('backend/chargeapp/delete_item/<int:myid>/', delete_charge, name="delete_charge"),
    path('backend/chargeapp/edit_item/<int:myid>/', edit_charge, name="edit_charge"),
    path('backend/chargeapp/update_item/<int:myid>/', update_charge, name="update_charge"),

    path('api/add_to_cart/', AddToCartAPIView.as_view(), name='add_to_cart'),
    path('api/get_cart/', CartDetailsAPIView.as_view(), name='get_cart'),

    path('api/get_cart/main/', CartDetailsMainAPIView.as_view(), name='get_cart'),

    path('api/increase/', IncreaseQuantity.as_view(), name='increase'),
    path('api/decrease/', DecreaseQuantity.as_view(), name='decrease'),

    path('api/increase/main/', IncreaseQuantityMain.as_view(), name=''),
    path('api/decrease/main/', DecreaseQuantityMain.as_view(), name=''),


    path('api/remove-cart-item/', RemoveCartItem.as_view(), name='remove_cart_item'),
    path('api/get_total_price/', CartTotalPrice.as_view(), name='CartTotalPrice'),

]
