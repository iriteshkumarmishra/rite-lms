from rest_framework import serializers


class TextModuleSaveSerialzer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=5000)
    track_completion = serializers.BooleanField(required=False)
    categories = serializers.ListField(required=False)

class TextModuleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.CharField()
    type = serializers.IntegerField()
    author = serializers.CharField()
    created_at = serializers.DateTimeField()