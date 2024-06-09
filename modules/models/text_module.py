from django.db import models

from modules.models.module import Module
from accounts.models import User

class TextModule(models.Model):
    id = models.BigAutoField(primary_key=True)
    module_id = models.OneToOneField(Module, related_name='text_module', on_delete=models.PROTECT, db_column='module_id')
    track_completion = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='text_created', on_delete=models.PROTECT, db_column='created_by')
    updated_by = models.ForeignKey(User, related_name='text_updated', on_delete=models.PROTECT, db_column='updated_by', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'text_modules'