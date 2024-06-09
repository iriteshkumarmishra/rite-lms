from django.urls import path

from courses.views.course_view import CourseList, CourseDetails
from courses.views.course_registration_view import CourseRegistrationList

urlpatterns = [
    path('', CourseList.as_view(), name='courses'),
    path('<int:id>', CourseDetails.as_view(), name='courses-details'),
    path('registrations/', CourseRegistrationList.as_view(), name='course-registrations')
]