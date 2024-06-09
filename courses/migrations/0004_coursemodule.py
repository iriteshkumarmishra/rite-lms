# Generated by Django 5.0.6 on 2024-06-02 12:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_created_by_alter_course_deleted_by_and_more'),
        ('modules', '0006_alter_textmodule_module_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModule',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('display_order', models.IntegerField()),
                ('is_locked', models.BooleanField(default=False)),
                ('drip_fixed_date', models.DateField(null=True)),
                ('min_spent_time', models.IntegerField(help_text='in seconds', null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.course')),
                ('created_by', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.RESTRICT, related_name='course_mod_created', to=settings.AUTH_USER_MODEL)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module', to='modules.module')),
                ('updated_by', models.ForeignKey(db_column='updated_by', on_delete=django.db.models.deletion.RESTRICT, related_name='course_mod_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'course_modules',
            },
        ),
    ]