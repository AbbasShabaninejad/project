from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from .models import OTP, User
from .serializers import SendOTPSerializer, VerifyOTPSerializer, LoginSerializer, UserDetailSerializer
import random
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Device
from .serializers import DeviceSerializer

import ghasedakpack
SMS = ghasedakpack.Ghasedak("e3a0106d66cedad553afbd0d5b0dd8f8c9fa4dfee6170e5e3afa53841d95b7de")


class SendOTP(APIView):
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            otp = random.randint(1000, 9999)
            print(otp)
            OTP.objects.update_or_create(phone_number=phone_number, defaults={'otp': otp, 'created_at': timezone.now()})
            SMS.verification({'receptor': 'phone_number','type': '1','template': 'randcode','param1': otp})

            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTP(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data['otp']
            phone_number = serializer.validated_data['phone_number']
            try:
                otp_instance = OTP.objects.get(phone_number=phone_number, otp=otp)
                if timezone.now() - otp_instance.created_at > timedelta(minutes=10):
                    return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)

                user, created = User.objects.get_or_create(phone=phone_number)
                if created:
                    user.set_password(User.objects.make_random_password())
                    user.save()

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                otp_instance.delete()

                return Response({
                    'message': 'User verified successfully',
                    'access_token': access_token,
                    'refresh_token': str(refresh)
                }, status=status.HTTP_200_OK)
            except OTP.DoesNotExist:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            if phone_number and password:
                user = authenticate(phone=phone_number, password=password)
                if user:
                   refresh = RefreshToken.for_user(user)
                   return Response({
                      'refresh': str(refresh),
                      'access': str(refresh.access_token),
                    }, status=status.HTTP_200_OK)
            
                return Response({'error': "Unable to log in with provided credentials."}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'error': "Must include 'phone_number' and 'password'."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailUpdateView(generics.RetrieveUpdateAPIView):
    # queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class DeviceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DeviceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    devices = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)

