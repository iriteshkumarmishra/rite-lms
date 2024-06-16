from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = None
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False, default='')
    email_verified_at = models.DateTimeField(null=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True)
    last_login_ip = models.GenericIPAddressField(null=True)
    is_disabled = models.IntegerField(choices={(1, 1), (0, 0)}, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.BigIntegerField(null=True)
    updated_by = models.BigIntegerField(null=True)
    deleted_by = models.BigIntegerField(null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager() ## This is the new line in the User model. ##

    class Meta:
        db_table = 'users'
    

    def get_full_name(self):
        return self.first_name + " " + self.last_name



class StoreAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=10, default='US')

    class Meta():
        db_table = 'store_addresses'


class UserAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user_address', on_delete=models.CASCADE)
    address = models.ForeignKey(StoreAddress, related_name='account_address', on_delete=models.PROTECT)
    full_name = models.CharField(max_length=255, null=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta():
        db_table = 'user_addresses'


