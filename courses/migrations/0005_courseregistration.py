# Generated by Django 5.0.6 on 2024-06-02 18:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_coursemodule'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'not_started'), (2, 'in_progress'), (3, 'completed')])),
                ('access_status', models.BooleanField(default=True)),
                ('registered_on', models.DateTimeField()),
                ('started_on', models.DateTimeField(null=True)),
                ('completed_on', models.DateTimeField(null=True)),
                ('expire_on', models.DateTimeField(null=True)),
                ('last_accessed_on', models.DateTimeField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='registered_course', to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='registered_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'course_registrations',
            },
        ),
    ]