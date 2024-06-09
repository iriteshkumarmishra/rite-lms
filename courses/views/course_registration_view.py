from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class CourseRegistrationList(APIView):
    """
    List all course registrations 
    """
    permission_classes = [IsAuthenticated, ]
