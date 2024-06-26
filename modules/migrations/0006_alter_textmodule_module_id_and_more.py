# Generated by Django 5.0.6 on 2024-06-01 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_alter_videomodule_cover_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textmodule',
            name='module_id',
            field=models.OneToOneField(db_column='module_id', on_delete=django.db.models.deletion.PROTECT, related_name='text_module', to='modules.module'),
        ),
        migrations.AlterField(
            model_name='videomodule',
            name='module_id',
            field=models.OneToOneField(db_column='module_id', on_delete=django.db.models.deletion.PROTECT, related_name='video_module', to='modules.module'),
        ),
    ]
