#
from .views import *
from django.urls import path

urlpatterns = [
    path('backend/dashboard', dashboard , name="backend/dashboard"),
    # path('backend/login', login , name="backend/login"),
    path('backend/login/', login_view, name='backend/login'),
    path('backend/logout/', logout_view, name='backend/logout'),

    path('backend/verify-email/', verify_email, name='backend/verify_email'),
    path('backend/verify-otp/', verify_otp, name='verify_otp'),
    path('backend/change-password/', change_password, name='change_password'),
]
