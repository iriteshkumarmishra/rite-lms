# Generated by Django 5.0.6 on 2024-05-31 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_options_alter_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
