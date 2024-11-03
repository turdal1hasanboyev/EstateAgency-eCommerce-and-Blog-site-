from django.db import models
import re
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, phone_number, first_name, last_name, description, note, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError('Users must have a valid phone number')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not description:
            raise ValueError('Users must have a description')
        if not note:
            raise ValueError('Users must have a note')
        if not password:
            raise ValueError('Users must have a password')
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, description=description, note=note, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, first_name, last_name, description, note, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not email:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError('Users must have a valid phone number')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not description:
            raise ValueError('Users must have a description')
        if not note:
            raise ValueError('Users must have a note')
        if not password:
            raise ValueError('Users must have a password')
        
        user = self.create_user(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, description=description, note=note, password=password, **extra_fields)
        return user


class CustomUser(AbstractUser, BaseModel):
    GENDER = (
        ('Erkak', ('Erkak')),
        ('Ayol', ('Ayol')),
    )
    username = None
    email = models.EmailField(unique=True)
    description = RichTextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='user_profile_pictures', default='img/user-default-image.jpg', null=True, blank=True)
    profile_video = models.FileField(upload_to='user_profile_videos', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    adress = RichTextField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    note = models.CharField(max_length=50, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'phone_number',
        'first_name',
        'last_name',
        'description',
        'note',
        ]
    
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        if self.get_full_name():
            return f"{self.get_full_name()}"
        return F"{self.email}"