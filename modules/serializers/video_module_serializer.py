from rest_framework import serializers

class VideoModuleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.CharField()
    type = serializers.IntegerField()
    provider = serializers.IntegerField()
    icon = serializers.CharField()
    author = serializers.CharField()
    created_at = serializers.DateTimeField()


class VideoModuleSaveSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    slug = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=3000)
    provider = serializers.ChoiceField(choices=[1, 2])
    url = serializers.CharField()
    cover_url = serializers.CharField(required=False)
    track_completion = serializers.BooleanField(required=False)
    disable_skip = serializers.BooleanField(required=False)
