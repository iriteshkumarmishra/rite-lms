# Generated by Django 5.0.6 on 2024-06-15 19:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_storeaddress_useraddress'),
        ('store', '0004_alter_cart_cart_settings_alter_product_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'payment_pending'), (2, 'completed'), (3, 'canceled'), (4, 'refunded'), (5, 'failed')])),
                ('coupon_used', models.CharField(max_length=255, null=True)),
                ('transaction_reference', models.CharField(max_length=255)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tax', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('test_order', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_billing_address', to='accounts.useraddress')),
                ('created_by', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.RESTRICT, related_name='order_creator', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(db_column='updated_by', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='order_updator', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'store_orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField(default=1)),
                ('price_per_qty', models.DecimalField(decimal_places=2, max_digits=5)),
                ('item_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_item_creator', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_order', to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_product', to='store.order')),
            ],
            options={
                'db_table': 'store_order_items',
            },
        ),
    ]
