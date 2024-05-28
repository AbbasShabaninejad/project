
from django.urls import path
from .views import SendOTP, VerifyOTP,LoginAPIView, UserDetailUpdateView, DeviceListCreateAPIView, DeviceRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('send-otp/', SendOTP.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTP.as_view(), name='verify-otp'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', UserDetailUpdateView.as_view(), name='user-detail-update'),
    #### for test and get token in test
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ####
    path('devices/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyAPIView.as_view(), name='device-detail'),
]
