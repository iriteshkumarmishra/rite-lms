from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

from courses.models.course import Course
from courses.serializers.course_serializer import CourseSerializer, EmptyCourseSerializer, CourseSaveSerializer
from core.paginations import DefaultPagination
from courses.services.course_service import CourseService

# Create your views here.

class CourseList(APIView, DefaultPagination):
    """
    List all courses or create a new course
    """

    permission_classes = [IsAuthenticated, ]
    # pagination_class = DefaultPagination ## Not required cause in APIView(non-generic) It doesn't work, need custom 

    def get(self, request):
        courses = Course.objects.all()
        results = self.paginate_queryset(courses, request, view=self)
        serializer = CourseSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        if request.data['status'] == Course.STATUS_DRAFT:
            serializer = EmptyCourseSerializer(data=request.data)
        else:
            serializer = CourseSaveSerializer(data=request.data)
        
        if serializer.is_valid():
            course_service = CourseService()
            response = course_service.create_course(serializer.validated_data, request.user)
            if response['success']:
                return Response('Course created', status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

class CourseDetails(APIView):
    """
    View, Update or Delete a course
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        course = Course.objects.filter(pk=pk).first()
        if course is None:
            raise Http404
        
        return course

    def get(self, request, id):
        course = self.get_object(id)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        course = self.get_object(id)
        course.created_by = request.user
        course.updated_by = request.user
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        course = self.get_object(id)
        course.deleted_by = request.user
        course.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
