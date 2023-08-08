from rest_framework import serializers
from .models import LoginUser

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = '__all__'