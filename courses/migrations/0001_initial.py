# Generated by Django 5.0.6 on 2024-05-27 19:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=500)),
                ('featured_image_url', models.CharField(max_length=500, null=True)),
                ('instructions', models.TextField(null=True)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'draft'), (1, 'publish')], default=0)),
                ('min_passing_percentage', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('certificate_template_id', models.CharField(help_text='Comma separated cert template IDs', max_length=500, null=True)),
                ('grading_rules', models.PositiveSmallIntegerField(choices=[(0, 'no_grading'), (1, 'avg_all_modules'), (2, 'avg_specific_modules')], default=0)),
                ('duration_rules', models.PositiveSmallIntegerField(choices=[(0, 'unlimited'), (1, 'on_specific_date'), (2, 'x_days_after_start'), (3, 'x_days_after_enrollment')], default=0)),
                ('duration_specific_date', models.DateField(null=True)),
                ('duration_days', models.PositiveIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deleted', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
