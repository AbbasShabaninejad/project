from rest_framework import serializers
from .models import User
from .models import Device




class SendOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)

class VerifyOTPSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4)
    phone_number = serializers.CharField(max_length=11)

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=128)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname', 'phone', 'email', 'address']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'device_type', 'created_at', 'last_active']
