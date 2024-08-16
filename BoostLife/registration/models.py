from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.shortcuts import reverse
from django.utils import timezone
from decimal import Decimal
from django.conf import settings
import random
from django.contrib.auth.models import User
from django.conf import settings
from django.db import IntegrityError

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, name=None, referral_code=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')

        email = self.normalize_email(email)
        if self.model.objects.filter(email=email).exists():
            raise ValueError('A user with that email already exists.')

        user = self.model(email=email, name=name, referral_code=referral_code, **extra_fields)
        user.set_password(password)
        try:
            user.save(using=self._db)
        except IntegrityError:
            raise ValueError('A user with that email already exists.')

        return user

    def create_superuser(self, email, password=None, name=None, referral_code=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, name, referral_code, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField( unique=True)
    is_influencer = models.BooleanField(default=False)
    id= models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=15)  # You can adjust the max_length as needed.
    name = models.CharField(max_length=255,null=True)
    bio=models.CharField(max_length=255,default='')
    profile_photo=models.ImageField(upload_to='videos/', null=True, blank=True)
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    # password = models.CharField(max_length=128)  # Store the password as a hash.
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)
    blocked_users = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='users_blocked_by')
    status = models.BooleanField(default=True)
    # walet=models.FloatField(default=11)
    gender = models.CharField(max_length=10,default='NA')
    age = models.CharField(max_length=255, default='0')
    height = models.CharField(max_length=255, default='0')
    weight = models.CharField(max_length=255, default='0')
    activity_level = models.CharField(max_length=255,default='0')
    # referral_link = models.CharField(max_length=255, blank=True, null=True, unique=True)
    # slug = models.CharField(max_length=15, blank=True,unique=True, null=True)
    objects = CustomUserManager()
    # total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    level = models.PositiveIntegerField(default=1)
    goal=models.CharField(max_length=255,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # def save(self, *args, **kwargs):
    #     if not self.walet:
    #         self.walet = 11.0
    #     super().save(*args, **kwargs)



    #
    #
    #     super(CustomUser, self).save(*args, **kwargs)
    #     super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return True  # Custom implementation if needed

    def has_module_perms(self, app_label):
        return True  # Custom implementation if needed
    def __str__(self):
        return f"{self.email}"
    class Meta:
        ordering = ['email']  # Adjust ordering field

class Otp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    email_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    newname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    delivery_time=models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newname