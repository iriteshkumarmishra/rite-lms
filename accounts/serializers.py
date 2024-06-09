from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta): 
        fields = ['id', 'first_name', 'email', 'password']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta): 
        fields = ['id', 'first_name', 'email', 'last_name', 'date_joined']

class CurrentUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta): 
        fields = ['id', 'first_name', 'email', 'last_name', 'date_joined']