from django.db import models

from courses.models.course import Course
from modules.models.module import Module
from accounts.models import User

class CourseModule(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    module = models.ForeignKey(Module, related_name='module', on_delete=models.CASCADE)
    display_order = models.IntegerField()
    is_locked = models.BooleanField(default=False)
    drip_fixed_date = models.DateField(null=True)
    min_spent_time = models.IntegerField(null=True, help_text='in seconds')
    created_by = models.ForeignKey(User, related_name='course_mod_created', on_delete=models.RESTRICT, db_column='created_by')
    updated_by = models.ForeignKey(User, related_name='course_mod_updated', on_delete=models.RESTRICT, db_column='updated_by')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta():
        db_table = 'course_modules'
