from django.db import models

from modules.models.module import Module
from accounts.models import User

class VideoModule(models.Model):
    id = models.BigAutoField(primary_key=True)
    module_id = models.OneToOneField(Module, related_name='video_module', on_delete=models.PROTECT, db_column='module_id')
    provider = models.SmallIntegerField(choices=[(1, 'youtube'), (2, 'in-house')])
    url = models.CharField(max_length=512)
    cover_url = models.CharField(max_length=512, null=True)
    disable_skip = models.BooleanField(default=True)
    track_completion = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='video_created', on_delete=models.PROTECT, db_column='created_by')
    updated_by = models.ForeignKey(User, related_name='video_updated', on_delete=models.PROTECT, db_column='updated_by', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'video_modules'