# Generated by Django 5.0.6 on 2024-05-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_is_active_alter_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='updated_by',
            field=models.BigIntegerField(null=True),
        ),
    ]