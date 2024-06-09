from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from modules.models.module import Module
from core.paginations import DefaultPagination
from modules.serializers.module_serializer import ModuleSerialzer

class ModulesList(APIView, DefaultPagination):
    """
    List all modules or create a new module
    """

    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        modules = Module.objects.all()
        results = self.paginate_queryset(modules, request)
        serializer = ModuleSerialzer(results, many=True)
        data = self.get_paginated_response(serializer.data)
        return data
    