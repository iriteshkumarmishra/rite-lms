from django.db import models

from accounts.models import User, UserAddress
from courses.models.course import Course

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    description = models.TextField()
    image_url = models.CharField(null=True, max_length=255)
    regular_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(choices=[(1, 'COMING-SOON'), (2, 'IN-STOCK'), (3, 'OUT-OF-STOCK')], default=2)
    expired_at = models.DateTimeField(null=True)
    seo_title = models.CharField(max_length=500, null=True)
    seo_description = models.CharField(max_length=500, null=True)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.RESTRICT, db_column='created_by')
    updated_by = models.ForeignKey(User, related_name='product_update', on_delete=models.RESTRICT, db_column='updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'store_products'
    
    def get_price(self):
        return self.sale_price
    
    def get_display_price(self):
        # for now we will just use sale_price later we will allow for great sales date
        return '{:.2f}'.format(self.sale_price)


class ProductCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='course_product')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='product_course')
    created_by = models.ForeignKey(User, related_name='product_course_creator', on_delete=models.RESTRICT, db_column='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'store_product_courses'


class Cart(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    cart_data = models.TextField()
    cart_settings = models.JSONField(null=True)


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField(choices=[(1, 'payment_pending'), (2, 'completed'), (3, 'canceled'), (4, 'refunded'), (5, 'failed')])
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.DO_NOTHING)
    billing_address = models.ForeignKey(UserAddress, related_name='user_billing_address', on_delete=models.DO_NOTHING)
    coupon_used = models.CharField(null=True, max_length=255)
    transaction_reference = models.CharField(max_length=255)
    sub_total = models.DecimalField(decimal_places=2, max_digits=6)
    tax = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    total = models.DecimalField(decimal_places=2, max_digits=6)
    test_order = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='order_creator', on_delete=models.RESTRICT, db_column='created_by')
    updated_by = models.ForeignKey(User, related_name='order_updator', on_delete=models.RESTRICT, db_column='updated_by', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'store_orders'


class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='item_order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='item_product', on_delete=models.DO_NOTHING)
    qty = models.IntegerField(default=1)
    price_per_qty = models.DecimalField(decimal_places=2, max_digits=5)
    item_total = models.DecimalField(decimal_places=2, max_digits=5)
    created_by = models.ForeignKey(User, related_name='order_item_creator', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'store_order_items'
