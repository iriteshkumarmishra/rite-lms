# Generated by Django 5.0.6 on 2024-06-03 19:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.RESTRICT, related_name='product_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_by',
            field=models.ForeignKey(db_column='updated_by', on_delete=django.db.models.deletion.RESTRICT, related_name='product_update', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productcourse',
            name='created_by',
            field=models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.RESTRICT, related_name='product_course_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='product',
            table='store_products',
        ),
        migrations.AlterModelTable(
            name='productcourse',
            table='store_product_courses',
        ),
    ]