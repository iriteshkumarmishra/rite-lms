from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta): 
        fields = ['id', 'first_name', 'email', 'password']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta): 
        fields = ['id', 'first_name', 'email', 'last_name', 'date_joined']

class CurrentUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta): 
        fields = ['id', 'first_name', 'email', 'last_name', 'date_joined']


class BillingAddressDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    is_default = serializers.BooleanField()
    full_name = serializers.CharField()
    address_line_1 = serializers.CharField()
    address_line_2 = serializers.CharField(required=False)
    zip = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField(max_length=2)
    country = serializers.CharField(max_length=5)
