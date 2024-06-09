from rest_framework.serializers import ModelSerializer

from modules.models.module import Module

class ModuleSerialzer(ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

        read_only_fields = ['created_by', 'updated_by']