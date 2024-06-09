from django.db import models

from accounts.models import User

# Create your models here.

class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    featured_image_url = models.CharField(null=True, max_length=500)
    instructions = models.TextField(null=True)
    credits = models.DecimalField(null=True, decimal_places=2, max_digits=3)
    is_archived = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(default=0, choices=[(0, 'draft'), (1, 'publish')])
    min_passing_percentage = models.DecimalField(null=True, decimal_places=2, max_digits=3)
    certificate_template_id = models.CharField(null=True, max_length=500, help_text='Comma separated cert template IDs')
    grading_rules = models.PositiveSmallIntegerField(default=0, choices=[(0, 'no_grading'), (1, 'avg_all_modules'), (2, 'avg_specific_modules')])
    duration_rules = models.PositiveSmallIntegerField(default=0, choices=[(0, 'unlimited'), (1, 'on_specific_date'), (2, 'x_days_after_start'), (3, 'x_days_after_enrollment')])
    duration_specific_date = models.DateField(null=True)
    duration_days = models.PositiveIntegerField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created', db_column='created_by')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='updated', db_column='updated_by')
    deleted_by = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='deleted', db_column='deleted_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'courses'

    # model constants
    STATUS_DRAFT = 0
    STATUS_PUBLISH = 1

    GRADE_RULE_NO_GRADING = 0
    GRADE_RULE_AVG_ALL_MODULES = 1
    GRADE_RULE_AVG_SPECIFIC_MODULES = 2

    DURATION_RULE_UNLIMITED = 0
    DURATION_RULE_ON_SPECIFIC_DATE = 1
    DURATION_RULE_DAYS_AFTER_START = 2
    DURATION_RULE_DAYS_AFTER_ENROLLMENT = 3






