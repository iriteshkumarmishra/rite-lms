from django.db import models

from courses.models.course import Course
from accounts.models import User

class CourseRegistration(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.ForeignKey(Course, related_name='registered_course', on_delete=models.RESTRICT)
    user = models.ForeignKey(User, related_name='registered_user', on_delete=models.RESTRICT)
    status = models.IntegerField(choices=[(1, 'not_started'), (2, 'in_progress'), (3, 'completed')])
    access_status = models.BooleanField(default=True)
    registered_on = models.DateTimeField()
    started_on = models.DateTimeField(null=True)
    completed_on = models.DateTimeField(null=True)
    expire_on = models.DateTimeField(null=True)
    last_accessed_on = models.DateTimeField(null=True)

    class Meta():
        db_table = 'course_registrations'
