# Generated by Django 5.0.6 on 2024-06-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('cart_data', models.TextField()),
                ('cart_settings', models.JSONField()),
            ],
        ),
    ]
