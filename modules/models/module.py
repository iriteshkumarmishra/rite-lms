from django.db import models

from accounts.models import User


class Module(models.Model):

    # def __init__(self):
    #     self.author = self.created_by

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    description = models.TextField(null=True)
    module_type_choices = [
        (1, 'text'),
        (2, 'pdf'),
        (3, 'video'),
        (4, 'webinar'),
        (5, 'scorm'),
        (6, 'quiz'),
        (7, 'assignment'),
        (8, 'survey'),
    ]
    type = models.SmallIntegerField(choices=module_type_choices)
    created_by = models.ForeignKey(User, db_column='created_by', related_name='m_created', on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User, db_column='updated_by', related_name='m_updated', on_delete=models.PROTECT, null=True)
    deleted_by = models.ForeignKey(User, db_column='deleted_by', related_name='m_deleted', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'modules'

    # Model constants
    TYPE_TEXT = 1
    TYPE_PDF = 2
    TYPE_VIDEO = 3
    TYPE_WEBINAR = 4
    TYPE_SCORM = 5
    TYPE_QUIZ = 6
    TYPE_ASSIGNMENT = 7
    TYPE_SURVEY = 8

    def get_icon(self):
        icon = ""
        type = self.type
        match type:
            case 1: icon = 'text-icon'
            case 2: icon = 'pdf-icon'
            case 3: icon = 'video-icon'
            case 4: icon = 'webinar-icon'
            case 5: icon = 'scorm-icon'
            case 6: icon = 'quiz-icon'
            case 7: icon = 'assignment-icon'
            case 8: icon = 'survey-icon'
        
        return icon