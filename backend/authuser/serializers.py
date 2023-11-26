from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from .models import User
from .custom_serializers import CustomTokenObtainPairSerializer



# User = get_user_model()


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email',  'password','name','address','date_joined','s_email','phone']

class MyTokenObtainPairSerializer(CustomTokenObtainPairSerializer):
    pass        