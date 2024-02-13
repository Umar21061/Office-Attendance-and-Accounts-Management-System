#The code imports necessary modules and classes from Django
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
#A custom user manager class, CustomUserManager, is defined, inheriting from Django's BaseUserManager

class CustomUserManager(BaseUserManager):


#Two methods :create_user for creating a regular user and create_superuser for creating a superuser.
    
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True or extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff=True and is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)
#A custom user model, CustomUser, is defined, inheriting from Django's AbstractBaseUser and PermissionsMixin.
class CustomUser(AbstractBaseUser, PermissionsMixin):
#The custom user model includes fields such as email, username, is_active, is_staff, and date_joined    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
#enabling custom methods for user management
    objects = CustomUserManager()
#specifies which fields are required when creating a user
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
#return the email address as the string 
    def __str__(self):
        return self.email
