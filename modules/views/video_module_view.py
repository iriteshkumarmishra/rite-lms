from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from modules.models.module import Module
from core.paginations import DefaultPagination
from accounts.models import User
from modules.serializers.video_module_serializer import VideoModuleSerializer, VideoModuleSaveSerializer
from modules.services.video_module_service import VideoService


class VideoModuleList(APIView, DefaultPagination):
    """
    List all video modules or create a vidoe module
    """

    permission_classes = [IsAuthenticated, ]

    def __init__(self):
        self.video_service = VideoService()
        super().__init__()

    def get(self, request):
        modules = Module.objects.filter(type=Module.TYPE_VIDEO).select_related('video_module')
        results = self.paginate_queryset(modules, request)
        response = []
        if results is not None:
            for data in results:
                author = User.objects.get(pk=1)
                setattr(data, 'author', author.first_name +' '+ author.last_name)
                setattr(data, 'provider', data.video_module.provider)
                setattr(data, 'icon', data.get_icon())
                response.append(data)
        
        serializer = VideoModuleSerializer(response, many=True)
        return self.get_paginated_response(serializer.data)
    

    def post(self, request):
        serializer = VideoModuleSaveSerializer(data=request.data)
        if serializer.is_valid():
            video_module = self.video_service.create_module(serializer.validated_data, request)
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class VideoModuleDetails(APIView):
    """
    View, Edit or Delete a video module
    """

    permission_classes = [IsAuthenticated, ]

    def get_object(self, id):
        try:
            object = Module.objects.get(pk=id)
            return object
        except Module.DoesNotExist:
            raise Http404

    def get(self, request, id):
        module = self.get_object(id)
        response = {
            'id': module.id,
            'name': module.name,
            'slug': module.slug,
            'description': module.description,
            'url': module.video_module.url,
            'provider': module.video_module.provider,
            'disable_skip': module.video_module.disable_skip,
            'track_completion': module.video_module.track_completion,
        }

        serializer = VideoModuleSaveSerializer(response)
        return Response(serializer.data, status=status.HTTP_200_OK)