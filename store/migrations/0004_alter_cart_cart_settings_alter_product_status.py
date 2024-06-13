# Generated by Django 5.0.6 on 2024-06-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_created_by_alter_product_updated_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_settings',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(1, 'COMING-SOON'), (2, 'IN-STOCK'), (3, 'OUT-OF-STOCK')], default=2),
        ),
    ]
