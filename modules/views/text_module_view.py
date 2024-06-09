from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from core.paginations import DefaultPagination
from accounts.models import User
from modules.serializers.text_module_serializer import TextModuleSerializer, TextModuleSaveSerialzer
from modules.models.text_module import TextModule
from modules.models.module import Module
from modules.services.text_module_service import TextModuleService

class TextModuleList(APIView, DefaultPagination):
    """
    List a text module or create a text module
    """

    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        text_modules = Module.objects.filter(type=Module.TYPE_TEXT)
        results = self.paginate_queryset(text_modules, request)
         # adding author data inside the results
        response = []
        if results is not None:
            for data in results:
                temp_user = User.objects.get(pk=1)
                setattr(data, 'author', temp_user.first_name + ' ' + temp_user.last_name)
                response.append(data)
        
        serializer = TextModuleSerializer(response, many=True)
        
        data = self.get_paginated_response(serializer.data)
        return data
    
    def post(self, request):
        # validating the request
        serializer = TextModuleSaveSerialzer(data=request.data)
        if serializer.is_valid():
            text_service = TextModuleService()
            text_module = text_service.create_text_module(serializer.validated_data, request)
            if text_module is not None:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response('Something went wrong', status=status.HTTP_400_BAD_REQUEST)
            
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
